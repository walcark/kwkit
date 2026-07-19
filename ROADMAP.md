# kwkit - Roadmap

Personal reusable toolbox, grown one stabilised routine at a time. The point is
to stop rewriting the same small helpers and pull them into demos and quick
tests instead. Scope grows on demand; organisation must not rot.

## Principles

- **Only stabilised, tested code lands here.** Drafts stay in scripts.
- **Light core, optional extras.** `import kwkit` pulls numpy at most; heavy
  dependencies live behind extras (`viz`, `ml`, `big`) and lazy submodules.
- **Organised by domain, not by type.** No `utils.py` grab-bag.
- **Every addition ships with tests** and passes `pixi run all`.

## Status by domain

| Domain | Status | Notes |
|---|---|---|
| `core` | started | dependency-light foundation (e.g. `unit_vector`) |
| `viz` | socle done | see below |
| `optics` | placeholder | ray geometry, radiometry, phase functions |
| `montecarlo` | placeholder | sampling, estimators, convergence diagnostics |
| `atmo` | placeholder | profiles, radiative-transfer helpers |

## viz

The plumbing layer is in place: a thin, composable wrapper over matplotlib and
SciencePlots that removes the recurring boilerplate without hiding matplotlib
(the escape hatch is always there). It follows three rules: every helper takes
an optional `ax` and returns it, nothing calls `show`/`savefig` behind your back
(except the explicit `save`), and styling is scoped through a context manager
rather than mutating globals. The socle ships `style()` (stacking SciencePlots
`science` + `no-latex` + a personal `kwkit.mplstyle` overlay, with a `latex=True`
opt-in for publication figures), `figure()` (subplots with constrained layout),
`colorbar()` (well-aligned, no `make_axes_locatable` dance), and `save()`
(reproducible multi-format export). The `kwkit.mplstyle` overlay ships empty on
purpose and is filled at use, one line at a time, as annoyances show up. Next
come the recurring *recipes* built on this socle: `heatmap2d` (imshow with
`origin`/`extent`/`aspect` pitfalls solved), `band` (confidence envelopes),
`profile` (quantity vs altitude, Y-axis inverted), plus domain plots such as
Monte-Carlo `convergence` and optics `phase_function`. Longer term, optional
paths worth evaluating: seaborn for statistical recipes and an xarray-first
route for atmospheric fields.

## Backlog (cross-cutting)

- Coverage badge goes live once the GitHub remote and Codecov are wired
  (`CODECOV_TOKEN`).
- Refine mypy strictness in a dedicated session.
- Consider `pre-commit` framework parity if the native git hook proves limiting.
