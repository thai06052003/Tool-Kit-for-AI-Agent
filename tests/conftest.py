"""Shared pytest fixtures for the migration test suite.

Provides ``tmp_path``-based source (``.agent/``) and target (``.kiro/``)
directory trees so individual tests can exercise translators and the writer
against real, throwaway file systems without touching the repository.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Register a Hypothesis profile so property tests run at least 100 examples
# (mirrors the [tool.hypothesis] note in pyproject.toml). Guarded so the suite
# still imports cleanly if Hypothesis is not installed.
try:
    from hypothesis import settings

    settings.register_profile("default", max_examples=100)
    settings.load_profile("default")
except ImportError:  # pragma: no cover - hypothesis optional at collection time
    pass


@pytest.fixture
def source_root(tmp_path: Path) -> Path:
    """An empty ``.agent/`` source tree with the standard sub-directories.

    Returns the path to a freshly created ``<tmp>/.agent`` directory containing
    empty ``agents/``, ``skills/``, ``rules/``, ``workflows/``, ``hooks/`` and
    ``scripts/`` sub-directories. Tests populate it as needed.
    """
    root = tmp_path / ".agent"
    for sub in ("agents", "skills", "rules", "workflows", "hooks", "scripts"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    return root


@pytest.fixture
def target_root(tmp_path: Path) -> Path:
    """An empty ``.kiro/`` target tree with the standard sub-directories.

    Returns the path to a freshly created ``<tmp>/.kiro`` directory containing
    empty ``agents/``, ``skills/``, ``steering/``, ``hooks/``, ``settings/`` and
    ``scripts/python/`` sub-directories.
    """
    root = tmp_path / ".kiro"
    for sub in ("agents", "skills", "steering", "hooks", "settings", "scripts/python"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    return root


@pytest.fixture
def make_agent(source_root: Path):
    """Factory creating an Antigravity agent ``.md`` file in ``source_root``.

    Usage::

        path = make_agent("backend-specialist", tools="Read, Bash", model="inherit")
    """

    def _make(
        name: str,
        *,
        tools: str = "Read, Grep, Bash",
        model: str = "inherit",
        skills: str | None = "skill-a, skill-b",
        description: str = "An example agent.",
        body: str = "# Body\n\nAgent instructions.\n",
    ) -> Path:
        lines = ["---", f"name: {name}", f"description: {description}"]
        if tools is not None:
            lines.append(f"tools: {tools}")
        if model is not None:
            lines.append(f"model: {model}")
        if skills is not None:
            lines.append(f"skills: {skills}")
        lines.append("---")
        content = "\n".join(lines) + "\n" + body
        path = source_root / "agents" / f"{name}.md"
        path.write_text(content, encoding="utf-8")
        return path

    return _make


@pytest.fixture
def make_skill(source_root: Path):
    """Factory creating an Antigravity skill folder with a ``SKILL.md`` file.

    Returns the path to the skill's ``SKILL.md``. Optional sub-directories
    (``scripts``, ``references``, ``assets``) can be requested via ``subdirs``.
    """

    def _make(
        name: str,
        *,
        frontmatter: str | None = None,
        body: str = "Skill body.\n",
        subdirs: tuple[str, ...] = (),
    ) -> Path:
        skill_dir = source_root / "skills" / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        if frontmatter is None:
            frontmatter = f"---\nname: {name}\ndescription: Example skill {name}.\n---\n"
        (skill_dir / "SKILL.md").write_text(frontmatter + body, encoding="utf-8")
        for sub in subdirs:
            sub_dir = skill_dir / sub
            sub_dir.mkdir(parents=True, exist_ok=True)
            (sub_dir / "placeholder.txt").write_text("data", encoding="utf-8")
        return skill_dir / "SKILL.md"

    return _make


@pytest.fixture
def make_hooks_json(source_root: Path):
    """Factory writing a Claude-style ``hooks.json`` into ``source_root/hooks``."""

    def _make(payload: dict | None = None) -> Path:
        if payload is None:
            payload = {
                "hooks": {
                    "SessionStart": [
                        {
                            "type": "command",
                            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/session_manager.py",
                        }
                    ]
                }
            }
        path = source_root / "hooks" / "hooks.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return path

    return _make


@pytest.fixture
def make_mcp_config(source_root: Path):
    """Factory writing an ``mcp_config.json`` (optionally with secrets) to source."""

    def _make(payload: dict | None = None) -> Path:
        if payload is None:
            payload = {
                "mcpServers": {
                    "example": {
                        "command": "node",
                        "args": ["server.js"],
                        "env": {"API_KEY": "super-secret-value"},
                        "disabled": False,
                    }
                }
            }
        path = source_root / "mcp_config.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return path

    return _make
