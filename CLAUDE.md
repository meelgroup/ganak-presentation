# CLAUDE.md

Beamer talk on Ganak (`presentation.tex`). Build with `latexmk -pdf presentation.tex`.

## Generated figures -- never edit the PDFs by hand
- `figs/mermaid/*.pdf` (main loop, descend, ascend): edit the `.mmd` sources, then
  `cd figs/mermaid && ./render.sh`. Do NOT call `mmdc` directly: `render.sh` gives
  Chromium a private fontconfig with TeX Live's Latin Modern Sans (the beamer font)
  and applies `config.json`.
- `figs/{cav-versions,cav-solvers,new-versions}.pdf` (cactus plots): `cd figs && ./make_figs.py`,
  reads `data/results.sqlite3`.

## Data
`data/results.sqlite3` is the run table of the plotted runs. The raw logs under `data/out-*`
and the full `data/data.sqlite3` are gitignored (too big); re-parse them with
`../scripts/data/get_data_ganak.py` from `data/`.
