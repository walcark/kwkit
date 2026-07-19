# kwkit

<p>
  <a href="https://github.com/walcark/kwkit/actions/workflows/ci.yml"><img src="https://github.com/walcark/kwkit/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://codecov.io/gh/walcark/kwkit"><img src="https://codecov.io/gh/walcark/kwkit/branch/main/graph/badge.svg"></a>
  <img src="https://img.shields.io/badge/python-3.11%2B-blue">
  <a href="https://pixi.sh"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
  <a href="https://mypy-lang.org/"><img src="https://img.shields.io/badge/mypy-checked-2a6db2"></a>
  <img src="https://img.shields.io/badge/tested%20with-pytest-0a9edc?logo=pytest&logoColor=white">
</p>

Personal reusable toolbox, organised by domain (optics, Monte-Carlo,
atmospheric science, generic algorithms). The goal: stop rewriting the same
small routines, and pull them into demos and quick tests instead.

## Design principles

- **Only stabilised, tested code lands here.** Drafts stay in scripts.
- **Light core.** `import kwkit` pulls numpy at most; heavy dependencies
  (matplotlib, torch, dask) live behind optional extras.
- **Lazy submodules.** Domain packages are imported on first access, so
  `import kwkit` never loads matplotlib or torch on its own.
- **Organised by domain, not by type.** No `utils.py` grab-bag.

## Install

```bash
pixi install                # core + dev env
pip install "kwkit[viz]"    # add plotting (matplotlib)
pip install "kwkit[all]"    # everything
```

Optional extras: `viz` (matplotlib), `ml` (torch), `big` (dask).

## Layout

```
src/kwkit/
    core/          # dependency-light foundation (numpy)
    optics/
    montecarlo/
    atmo/
    viz/           # requires kwkit[viz]
```

## Development

```bash
pixi run all        # fmt + lint + type-check + test
pixi run test
```

A versioned pre-commit hook (`.githooks/pre-commit`) runs `fmt-check` + `lint`
before each commit. Enable it once per clone:

```bash
git config core.hooksPath .githooks
```
