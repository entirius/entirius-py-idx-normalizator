# AGENTS.md

Identifier normalizer and validator — distribution `entirius-py-idx-normalizator`, import `idx_normalizator`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `idx_normalizator` — it is a public API contract.
- Default: do not commit — git is the user's call.

## Architecture

Functions in `idx_normalizator/`: `normalize_idx`/`validate_idx` (slugified index with md5
suffix when over `max_len`), `normalize_sku`/`validate_sku`, `normalize_ean`/`validate_ean`.
Runtime dependency: `python-slugify`.
