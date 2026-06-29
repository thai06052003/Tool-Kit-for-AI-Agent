"""Antigravity Kit -> Kiro migration tool.

This module translates an Antigravity Kit (``.agent/``) into a Kiro-compatible
layout (``.kiro/``). The migration follows a three-phase pipeline:

1. **Inventory** -- scan ``.agent/`` and record every component in
   ``inventory.json`` (name, type, source/dest paths, status, note).
2. **Translate** -- normalize each component (agents, skills, rules, workflows,
   hooks, MCP config, scripts) into its Kiro equivalent.
3. **Write** -- persist results non-destructively (never overwrite existing
   files in ``.kiro/``).

Design guarantees:

* **Non-destructive** -- the writer only ever creates new files.
* **Fail-soft** -- an error in one component does not stop the pipeline.
* **Idempotent** -- running the tool repeatedly yields the same result.
* **Cross-platform** -- all paths use :mod:`pathlib`.

See ``.kiro/specs/antigravity-kiro-integration/`` for the full spec.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

__version__ = "1.0.0"

# --------------------------------------------------------------------------- #
# Type aliases
# --------------------------------------------------------------------------- #

#: Valid lifecycle states for an inventory entry.
EntryStatus = Literal["pending", "translated", "skipped", "invalid"]

#: Valid component types discovered during the inventory scan.
EntryType = Literal["agent", "skill", "rule", "workflow", "hook", "mcp", "script"]


# --------------------------------------------------------------------------- #
# Data models
# --------------------------------------------------------------------------- #


@dataclass
class InventoryEntry:
    """A single component discovered in the source ``.agent/`` tree.

    Attributes:
        name: Logical name of the component (e.g. ``backend-specialist``).
        type: Component category. One of :data:`EntryType`.
        source_path: Absolute or relative path to the source artifact.
        dest_path: Computed destination path inside the target ``.kiro/`` tree.
        status: Current lifecycle state. One of :data:`EntryStatus`.
        note: Free-form note (e.g. reason for ``invalid``/``skipped``).
    """

    name: str
    type: EntryType
    source_path: Path
    dest_path: Path
    status: EntryStatus = "pending"
    note: str = ""


@dataclass
class TypeCount:
    """Per-type tally used inside :class:`InventorySummary`.

    Mirrors the nested objects of the ``summary`` block in ``inventory.json``
    (e.g. ``{"total": 61, "translated": 0, "skipped": 0, "invalid": 0}``).
    """

    total: int = 0
    translated: int = 0
    skipped: int = 0
    invalid: int = 0


@dataclass
class InventorySummary:
    """Aggregate counts mirroring the ``summary`` block of ``inventory.json``.

    The schema is defined in ``design.md``::

        "summary": {
          "agents":   {"total", "translated", "skipped", "invalid"},
          "skills":   {"total", "translated", "skipped", "invalid"},
          "steering": {"total", "translated", "skipped"},
          "hooks":    {"total", "translated", "skipped"},
          "errors":   0
        }

    ``steering`` aggregates both rules and workflows (they both land in
    ``.kiro/steering/``). ``errors`` is a flat counter for unrecoverable
    component failures.
    """

    agents: TypeCount = field(default_factory=TypeCount)
    skills: TypeCount = field(default_factory=TypeCount)
    steering: TypeCount = field(default_factory=TypeCount)
    hooks: TypeCount = field(default_factory=TypeCount)
    errors: int = 0


# --------------------------------------------------------------------------- #
# Inventory scanning
# --------------------------------------------------------------------------- #

#: Explicit source-stem -> destination-slug mapping for known rule files.
#: Any rule whose stem is not listed here falls back to a kebab-cased stem.
RULE_SLUG_MAP: dict[str, str] = {
    "GEMINI": "master-rules",
    "CONTEXT-INPUT": "context-input",
}


def _kebab_case(text: str) -> str:
    """Return a lowercase, hyphen-delimited slug for ``text``.

    Splits ``camelCase`` boundaries, collapses runs of whitespace, underscores
    and hyphens into a single hyphen, and trims leading/trailing hyphens.

    Examples:
        ``"MyCustomRule"`` -> ``"my-custom-rule"``
        ``"some_rule name"`` -> ``"some-rule-name"``
    """

    # Insert a hyphen between a lower/digit char and an uppercase char.
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", text)
    # Normalize any separator run (whitespace, underscore, hyphen) to one hyphen.
    slug = re.sub(r"[\s_-]+", "-", spaced)
    return slug.strip("-").lower()


class InventoryScanner:
    """Phase 1 of the migration pipeline.

    Walks the source ``.agent/`` tree and produces an :class:`InventoryEntry`
    for every component it understands, computing each component's destination
    path inside the target ``.kiro/`` tree from the mapping tables in
    ``design.md``.

    The scan is read-only: it never writes to disk. Entries whose ``dest_path``
    already exists are pre-marked ``skipped`` so the non-destructive writer in a
    later phase can short-circuit them.
    """

    @staticmethod
    def scan(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Scan ``source_root`` and return inventory entries.

        Args:
            source_root: Root of the Antigravity kit (e.g. ``.agent/``).
            target_root: Root of the Kiro layout (e.g. ``.kiro/``).

        Returns:
            A list of :class:`InventoryEntry`, one per discovered component,
            ordered by component type and then name for deterministic,
            idempotent output. Entries whose destination already exists have
            ``status="skipped"``; all others are ``"pending"``.
        """

        source_root = Path(source_root)
        target_root = Path(target_root)

        entries: list[InventoryEntry] = []
        entries.extend(InventoryScanner._scan_agents(source_root, target_root))
        entries.extend(InventoryScanner._scan_skills(source_root, target_root))
        entries.extend(InventoryScanner._scan_rules(source_root, target_root))
        entries.extend(InventoryScanner._scan_workflows(source_root, target_root))
        entries.extend(InventoryScanner._scan_hooks(source_root, target_root))
        entries.extend(InventoryScanner._scan_mcp(source_root, target_root))
        entries.extend(InventoryScanner._scan_scripts(source_root, target_root))

        for entry in entries:
            InventoryScanner._mark_if_exists(entry)

        return entries

    # ------------------------------------------------------------------ #
    # Per-type scanners
    # ------------------------------------------------------------------ #

    @staticmethod
    def _scan_agents(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``agents/*.md`` -> ``<target>/agents/<name>.md``."""
        agents_dir = source_root / "agents"
        entries: list[InventoryEntry] = []
        for source_path in sorted(agents_dir.glob("*.md")):
            name = source_path.stem
            entries.append(
                InventoryEntry(
                    name=name,
                    type="agent",
                    source_path=source_path,
                    dest_path=target_root / "agents" / f"{name}.md",
                )
            )
        return entries

    @staticmethod
    def _scan_skills(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``skills/*/SKILL.md`` -> ``<target>/skills/<name>/``.

        ``source_path`` points at the ``SKILL.md`` file while ``dest_path`` is
        the destination skill *directory* (the whole tree is copied later).
        """
        skills_dir = source_root / "skills"
        entries: list[InventoryEntry] = []
        for source_path in sorted(skills_dir.glob("*/SKILL.md")):
            name = source_path.parent.name
            entries.append(
                InventoryEntry(
                    name=name,
                    type="skill",
                    source_path=source_path,
                    dest_path=target_root / "skills" / name,
                )
            )
        return entries

    @staticmethod
    def _scan_rules(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``rules/*.md`` -> ``<target>/steering/antigravity-<slug>.md``.

        Known rule stems use :data:`RULE_SLUG_MAP`; any other stem falls back to
        its kebab-cased form.
        """
        rules_dir = source_root / "rules"
        entries: list[InventoryEntry] = []
        for source_path in sorted(rules_dir.glob("*.md")):
            stem = source_path.stem
            slug = RULE_SLUG_MAP.get(stem, _kebab_case(stem))
            entries.append(
                InventoryEntry(
                    name=stem,
                    type="rule",
                    source_path=source_path,
                    dest_path=target_root / "steering" / f"antigravity-{slug}.md",
                )
            )
        return entries

    @staticmethod
    def _scan_workflows(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``workflows/*.md`` -> ``<target>/steering/workflow-<name>.md``."""
        workflows_dir = source_root / "workflows"
        entries: list[InventoryEntry] = []
        for source_path in sorted(workflows_dir.glob("*.md")):
            name = source_path.stem
            entries.append(
                InventoryEntry(
                    name=name,
                    type="workflow",
                    source_path=source_path,
                    dest_path=target_root / "steering" / f"workflow-{name}.md",
                )
            )
        return entries

    @staticmethod
    def _scan_hooks(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``hooks/hooks.json`` -> ``<target>/hooks/session-start.kiro.hook``."""
        hooks_json = source_root / "hooks" / "hooks.json"
        if not hooks_json.is_file():
            return []
        return [
            InventoryEntry(
                name="session-start",
                type="hook",
                source_path=hooks_json,
                dest_path=target_root / "hooks" / "session-start.kiro.hook",
            )
        ]

    @staticmethod
    def _scan_mcp(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Detect ``mcp_config.json`` -> ``<target>/settings/mcp-antigravity.json.example``."""
        mcp_config = source_root / "mcp_config.json"
        if not mcp_config.is_file():
            return []
        return [
            InventoryEntry(
                name="mcp-antigravity",
                type="mcp",
                source_path=mcp_config,
                dest_path=target_root
                / "settings"
                / "mcp-antigravity.json.example",
            )
        ]

    @staticmethod
    def _scan_scripts(source_root: Path, target_root: Path) -> list[InventoryEntry]:
        """Discover ``scripts/*.py`` -> ``<target>/scripts/python/<file>``."""
        scripts_dir = source_root / "scripts"
        entries: list[InventoryEntry] = []
        for source_path in sorted(scripts_dir.glob("*.py")):
            entries.append(
                InventoryEntry(
                    name=source_path.stem,
                    type="script",
                    source_path=source_path,
                    dest_path=target_root
                    / "scripts"
                    / "python"
                    / source_path.name,
                )
            )
        return entries

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #

    @staticmethod
    def _mark_if_exists(entry: InventoryEntry) -> None:
        """Pre-mark an entry ``skipped`` when its destination already exists."""
        if entry.dest_path.exists():
            entry.status = "skipped"
            entry.note = "already exists"
