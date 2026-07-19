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

Optional extras: `viz` (matplotlib + scienceplots), `ml` (torch), `big` (dask).

## Plotting (`viz`)

Thin ergonomic layer over matplotlib and SciencePlots. Helpers take an optional
`ax` and return it, nothing calls `show`/`savefig` behind your back (except the
explicit `save`), and styling is scoped:

```python
from kwkit import viz

with viz.style():                       # science + no-latex + personal overlay
    fig, ax = viz.figure()
    img = ax.imshow(field)
    viz.colorbar(img, ax=ax, label="intensity")
    viz.save(fig, "figure", formats=["png", "pdf"])
```

`viz.style(latex=True)` switches to LaTeX rendering; `viz.style("ieee")` stacks
an extra SciencePlots preset. Personal rcParams live in
`src/kwkit/viz/kwkit.mplstyle`, stacked last so they win. It ships empty on
purpose: fill it one line at a time as recurring annoyances show up.

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
