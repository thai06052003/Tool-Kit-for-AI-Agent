# Implementation Plan: Antigravity Kit → Kiro Integration

## Overview

Implement `migrate_antigravity.py` — a Python 3.11+ migration tool that translates the Antigravity Kit (`.agent/`) into Kiro-compatible format (`.kiro/`). The tool follows a three-phase pipeline: Inventory → Translate → Write, with full non-destructive, fail-soft, and idempotent guarantees. Property-based tests (Hypothesis) validate the seven core correctness properties defined in the design.

---

## Tasks

- [x] 1. Set up project structure, data models, and test framework
  - Create `migrate_antigravity.py` at the workspace root with module-level docstring and `__version__ = "1.0.0"`
  - Create `tests/` directory with `__init__.py`, `tests/unit/__init__.py`, `tests/property/__init__.py`, `tests/integration/__init__.py`
  - Create `tests/conftest.py` with shared `tmp_path`-based fixtures for source/target directory trees
  - Add `pyproject.toml` (or `pytest.ini`) configuring pytest with `--cov=migrate_antigravity --cov-fail-under=80` and hypothesis settings (`max_examples=100`)
  - Define `InventoryEntry` dataclass with fields: `name`, `type`, `source_path: Path`, `dest_path: Path`, `status` (Literal `pending|translated|skipped|invalid`), `note: str`
  - Define `InventorySummary` dataclass mirroring the `summary` block in `inventory.json`
  - _Requirements: R1.1, R8.1_

- [ ] 2. Implement InventoryScanner
  - [-] 2.1 Implement `InventoryScanner.scan(source_root: Path, target_root: Path) -> list[InventoryEntry]`
    - Glob `agents/*.md` → type=`agent`, dest=`target_root/agents/<name>.md`
    - Glob `skills/*/SKILL.md` → type=`skill`, dest dir=`target_root/skills/<name>/`
    - Glob `rules/*.md` → type=`rule`, dest=`target_root/steering/antigravity-<slug>.md`
    - Glob `workflows/*.md` → type=`workflow`, dest=`target_root/steering/workflow-<name>.md`
    - Parse `hooks/hooks.json` → type=`hook`, dest=`target_root/hooks/session-start.kiro.hook`
    - Detect `mcp_config.json` → type=`mcp`, dest=`target_root/settings/mcp-antigravity.json.example`
    - Glob `scripts/*.py` → type=`script`, dest=`target_root/scripts/python/<file>`
    - Set `status=skipped` for entries whose `dest_path` already exists
    - _Requirements: R1.1, R1.2, R1.3_

  - [-] 2.2 Implement `InventoryScanner.write_inventory(entries, path: Path)` and `load_inventory(path: Path)`
    - Serialize to `inventory.json` with `meta` block (timestamp, source/target roots, version) and `summary` block
    - `load_inventory` deserialises back to `list[InventoryEntry]` for idempotent re-runs
    - _Requirements: R1.1_

  - [~] 2.3 Write unit tests for InventoryScanner
    - Test that each glob pattern produces the correct `type` and `dest_path`
    - Test that existing `dest_path` sets `status=skipped` without side effects
    - Test `write_inventory` / `load_inventory` round-trip
    - _Requirements: R1.1, R1.2_

- [ ] 3. Implement AgentTranslator
  - [~] 3.1 Implement `AgentTranslator.translate(entry: InventoryEntry) -> str`
    - Parse YAML frontmatter using `ruamel.yaml` or `PyYAML`
    - Convert `tools` CSV string → `list[str]` (strip whitespace per element)
    - Map `model: inherit` → `model: claude-sonnet-4-5`; leave all other model values unchanged
    - Remove `skills` key from frontmatter if present
    - Preserve body markdown verbatim (everything after closing `---`)
    - Return serialised file content (frontmatter block + body)
    - _Requirements: R2.1, R2.2_

  - [~] 3.2 Write property test for AgentTranslator (P3)
    - **Property 3: Agent frontmatter normalization**
    - `tools` output is always `list`, `model` output is never `"inherit"`, `skills` key absent, body unchanged
    - **Validates: Requirements 2.1, 2.2**
    - _Requirements: R2.1, R2.2_

  - [~] 3.3 Write unit tests for AgentTranslator
    - Test tools CSV → list (with spaces, empty string, single item)
    - Test model `inherit` → `claude-sonnet-4-5`
    - Test model other values preserved
    - Test `skills` key removal and body not modified
    - _Requirements: R2.1, R2.2_

- [ ] 4. Implement SkillTranslator
  - [~] 4.1 Implement `SkillTranslator.translate_batch(entries: list[InventoryEntry], batch_size: int = 100)`
    - For each skill entry: copy `source_path.parent/` directory tree to `dest_path` recursively (including `scripts/`, `references/`, `assets/`)
    - Detect missing or empty `name`/`description` in `SKILL.md` frontmatter → inject minimal frontmatter derived from directory name
    - Print batch progress `[Batch N/M] Skills X-Y...` to stdout
    - Skip entire directory if dest already exists (set `status=skipped`)
    - _Requirements: R3.1, R3.2, R3.3, R3.4_

  - [~] 4.2 Write property test for SkillTranslator (P6)
    - **Property 6: Skill frontmatter injection**
    - Result `SKILL.md` always has non-empty `name` and `description` fields after translation regardless of input
    - **Validates: Requirements 3.3**
    - _Requirements: R3.3_

  - [~] 4.3 Write unit tests for SkillTranslator
    - Test frontmatter injection when `name` missing
    - Test frontmatter injection when `description` missing
    - Test directory skip when dest already exists
    - _Requirements: R3.2, R3.3_

- [ ] 5. Implement RuleTranslator and WorkflowTranslator
  - [~] 5.1 Implement `RuleTranslator.translate(entry: InventoryEntry) -> str`
    - Prepend `inclusion: auto` frontmatter + `description` to rule file content
    - Map `GEMINI.md` → `antigravity-master-rules.md`, `CONTEXT-INPUT.md` → `antigravity-context-input.md`
    - _Requirements: R4.1, R4.2, R4.3_

  - [~] 5.2 Implement `WorkflowTranslator.translate(entry: InventoryEntry) -> str`
    - `orchestrate.md` → prepend frontmatter with `inclusion: auto`
    - All other workflows → prepend frontmatter with `inclusion: manual`
    - Add `description` field summarising the workflow purpose (derived from filename)
    - Preserve workflow body content verbatim
    - _Requirements: R5.1, R5.2, R5.3_

  - [~] 5.3 Write property test for WorkflowTranslator (P5)
    - **Property 5: Workflow inclusion routing**
    - Any input named `"orchestrate"` always produces `inclusion: auto`; all other names always produce `inclusion: manual`
    - **Validates: Requirements 4.1, 5.2**
    - _Requirements: R5.2_

  - [~] 5.4 Write unit tests for RuleTranslator and WorkflowTranslator
    - Test `orchestrate` → `auto`, arbitrary non-orchestrate name → `manual`
    - Test body content preserved verbatim after prepend
    - Test rule slug generation for each known rule filename
    - _Requirements: R4.1, R5.1, R5.2_

- [ ] 6. Implement HookTranslator and McpTranslator
  - [~] 6.1 Implement `HookTranslator.translate(hooks_json_path: Path) -> str`
    - Parse `hooks.json`, locate `SessionStart` trigger entry
    - Map trigger → `promptSubmit`
    - Replace `${CLAUDE_PLUGIN_ROOT}/...` references → `python .kiro/scripts/python/<script>`
    - Emit JSON conforming to `.kiro.hook` schema (version, name, description, enabled, when, then)
    - Return note string describing trigger mismatch for `inventory.json[note]`
    - _Requirements: R6.1, R6.2, R6.3_

  - [~] 6.2 Implement `McpTranslator.translate(mcp_config_path: Path) -> dict`
    - Strip `// ...` JS-style comments before JSON parsing
    - Recursively sanitize all dict values: if key matches `api_key|apiKey|token|secret|password|key` (case-insensitive) → replace value with `<YOUR_API_KEY_HERE>`
    - Preserve `command`, `args`, `disabled`, `autoApprove` fields unchanged
    - Return sanitised dict ready for `json.dumps`
    - _Requirements: R7.1, R7.2_

  - [~] 6.3 Write property test for McpTranslator (P7)
    - **Property 7: MCP secret sanitization**
    - For any dict with arbitrary key names: keys matching secret patterns always receive placeholder value; non-matching keys always keep original value
    - **Validates: Requirements 6.2**
    - _Requirements: R7.2_

  - [~] 6.4 Write unit tests for HookTranslator and McpTranslator
    - Test `SessionStart` → `promptSubmit` mapping produces valid `.kiro.hook` JSON
    - Test `${CLAUDE_PLUGIN_ROOT}` variable substitution
    - Test JS comment stripping before JSON parse
    - Test nested `env` dict sanitisation
    - Test non-secret fields preserved after sanitisation
    - _Requirements: R6.1, R6.2, R7.2_

- [ ] 7. Implement ScriptCopier and NonDestructiveWriter
  - [~] 7.1 Implement `ScriptCopier.copy(entries: list[InventoryEntry], target_root: Path)`
    - Copy each `*.py` file from `scripts/` → `.kiro/scripts/python/` via `NonDestructiveWriter`
    - Create `README.md` in `.kiro/scripts/python/` with Windows invocation examples: `python .kiro\scripts\python\checklist.py .`
    - _Requirements: R7.3_

  - [~] 7.2 Implement `NonDestructiveWriter.write(dest_path: Path, content: str | bytes) -> WriteResult`
    - If `dest_path.exists()` → return `WriteResult(status="skipped", note="already exists")` without touching the file
    - Otherwise: `dest_path.parent.mkdir(parents=True, exist_ok=True)`, write content with `encoding="utf-8"`, return `WriteResult(status="translated")`
    - _Requirements: R8.2, R9.1_

  - [~] 7.3 Write property test for NonDestructiveWriter (P1)
    - **Property 1: Non-destructive write**
    - For any pre-existing file, calling `write()` with any different content leaves the original file content unchanged
    - **Validates: Requirements 7.1, 8.2, 9.1**
    - _Requirements: R8.2, R9.1_

  - [~] 7.4 Write unit tests for NonDestructiveWriter
    - Test new file is created with correct content
    - Test existing file is not overwritten and returns `status=skipped`
    - Test intermediate directories are created automatically
    - _Requirements: R8.2, R9.1_

- [~] 8. Checkpoint — Core components complete
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 9. Implement fail-soft pipeline and idempotence
  - [~] 9.1 Implement `MigrationPipeline.run(entries: list[InventoryEntry])`
    - Iterate pending entries; dispatch to correct translator by `entry.type`
    - Wrap each translate+write call in `try/except Exception as e`; on error set `entry.status = "invalid"`, `entry.note = f"{type(e).__name__}: {e}"`, then continue
    - Handle `UnicodeDecodeError` with latin-1 fallback before marking invalid
    - Write updated `inventory.json` after all entries are processed
    - _Requirements: R8.4_

  - [~] 9.2 Write property test for fail-soft behavior (P4)
    - **Property 4: Fail-soft behavior**
    - For any mix of valid and invalid entries, pipeline processes all valid entries (status `translated` or `skipped`) and marks invalid entries as `invalid` without propagating exceptions
    - **Validates: Requirements 7.5, 1.3**
    - _Requirements: R8.4, R1.3_

  - [~] 9.3 Implement idempotence: re-run detection and AGENTS.md append
    - On second run `InventoryScanner` sets pre-existing dest files to `status=skipped`; `MigrationPipeline.run` skips `skipped` and `translated` entries
    - AGENTS.md append uses `<!-- ANTIGRAVITY-AGENTS-START -->` / `<!-- ANTIGRAVITY-AGENTS-END -->` markers; detect existing markers and skip append
    - _Requirements: R8.3, R9.2, R2.4_

  - [~] 9.4 Write property test for idempotence (P2)
    - **Property 2: Idempotence**
    - Running `migrate()` twice produces the same `.kiro/` file tree as running it once — no additional files, no overwritten content
    - **Validates: Requirements 8.3**
    - _Requirements: R8.3_

- [ ] 10. Implement CLI entry point and summary output
  - [~] 10.1 Implement `argparse` CLI in `if __name__ == "__main__"` block
    - Arguments: `--source PATH` (default `.agent/`), `--target PATH` (default `.kiro/`), `--dry-run`, `--verbose`
    - `--dry-run`: run InventoryScanner only, print summary, exit 0 without writing any files
    - `--verbose`: log each file action to stdout as it occurs
    - Exit code 0 on success (including entries with `invalid` status); exit code 1 only on unrecoverable startup error
    - _Requirements: R8.1, R8.5, R8.6_

  - [~] 10.2 Implement summary printer
    - Format: `Agents: X/Y | Skills: X/Y | Steering: X | Hooks: X | Skipped: N | Errors: N`
    - Derive counts from `inventory.json` summary block after run
    - _Requirements: R8.6_

  - [~] 10.3 Write unit tests for CLI and summary
    - Test `--dry-run` exits without writing any files
    - Test summary string matches the specified format
    - Test `--verbose` flag propagates through to writer
    - _Requirements: R8.5, R8.6_

- [ ] 11. Implement Hypothesis strategies and wire all property tests
  - [~] 11.1 Create `tests/property/strategies.py` with custom Hypothesis strategies
    - `agent_frontmatter_st()` — generates dicts with arbitrary `tools` (CSV string or list), `model` (including `"inherit"`), optional `skills` key
    - `workflow_name_st()` — generates arbitrary workflow names including `"orchestrate"`
    - `mcp_config_st()` — generates nested dicts with arbitrary keys, subset matching secret patterns
    - `inventory_entries_st(valid_ratio)` — generates mixed lists of valid/invalid entries for P4
    - _Requirements: Design Correctness Properties P1–P7_

  - [~] 11.2 Wire all 7 property tests in `tests/property/test_properties.py`
    - Import strategies from `strategies.py`
    - Decorate each test with `@given(...)` and `@settings(max_examples=100)`
    - Reference each property by number in docstring: `"""P1: Non-destructive write..."""`
    - _Requirements: Design Correctness Properties P1–P7_

- [ ] 12. Write integration test for full migration
  - [~] 12.1 Write `tests/integration/test_full_migration.py`
    - Build a minimal but realistic `.agent/` tree in `tmp_path` (2 agents, 3 skills, 1 rule, 1 workflow, `hooks.json`, `mcp_config.json`, 1 script)
    - Run migration via `MigrationPipeline` with `--source` / `--target` pointing to tmp dirs
    - Assert output file tree matches expected structure and content
    - Assert no pre-existing `.kiro/` files were modified (P1 integration check)
    - Run migration a second time and assert no new files created and no files changed (P2 integration check)
    - _Requirements: R8.2, R8.3, R9.1_

- [~] 13. Final checkpoint — Ensure all tests pass
  - Ensure all tests pass (`pytest tests/ --hypothesis-seed=0 --cov=migrate_antigravity --cov-fail-under=80`), ask the user if questions arise.

---

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP pass
- All property tests use `@given` + `@settings(max_examples=100)` with `hypothesis-seed=0` in CI for reproducibility
- `NonDestructiveWriter.write()` is the single choke-point enforcing R8.2 and R9.1 — all translators route through it
- Batch progress in SkillTranslator prints to stdout (not logging) to remain visible even without `--verbose`
- The AGENTS.md idempotent append (task 9.3) uses HTML comment markers so the block is detectable on re-runs
- `UnicodeDecodeError` latin-1 fallback lives in `MigrationPipeline.run`, not inside individual translators

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1", "2.2"] },
    { "id": 2, "tasks": ["2.3", "3.1", "4.1", "5.1", "5.2", "6.1", "6.2", "7.1", "7.2"] },
    { "id": 3, "tasks": ["3.2", "3.3", "4.2", "4.3", "5.3", "5.4", "6.3", "6.4", "7.3", "7.4"] },
    { "id": 4, "tasks": ["9.1", "10.1", "10.2", "11.1"] },
    { "id": 5, "tasks": ["9.2", "9.3", "9.4", "10.3", "11.2"] },
    { "id": 6, "tasks": ["12.1"] }
  ]
}
```
