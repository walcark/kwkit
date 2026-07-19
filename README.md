# kwkit

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
