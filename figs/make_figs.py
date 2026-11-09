#!/usr/bin/env python3
# Cactus plots for the slides from data/data.sqlite3. Usage: cd figs && ./make_figs.py
import sqlite3
import subprocess

DB = "../data/results.sqlite3"
TOUT = 3600

COLORS = ["#7f7f7f", "#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#d62728"]

GRAPHS = {
    "cav-versions": dict(yr=(700, 1140), runs=[
        ("out-ganak-mc2324-14063135-1", "Ganak (2019)"),
        ("out-ganak-mc2324-14072353-1", "+ChronoBT +SAT"),
        ("out-ganak-mc2324-14063135-7", "+enhanced SAT"),
        ("out-ganak-mc2324-14063135-4", "+dual indep. set"),
        ("out-ganak-mc2324-14063135-0", "Ganak2 (CAV'25)"),
    ]),
    "cav-solvers": dict(yr=(700, 1140), runs=[
        ("out-ganak-mc2324-14063135-1", "Ganak (2019)"),
        ("out-others-gpmc", "gpmc"),
        ("out-others-d4", "d4"),
        ("out-ganak-mc2324-14063135-0", "Ganak2 (CAV'25)"),
    ]),
    "new-versions": dict(yr=(1100, 1225), xr=(500, TOUT), runs=[
        ("out-ganak-mccomp2324-1783906-0", "Jun 2026 baseline"),
        ("out-ganak-mccomp2324-2345011-2", "+new TD selection"),
        ("out-ganak-mccomp2324-2366186-3", "+TD flat/dense rules"),
        ("out-ganak-mccomp2324-2791823-2", "+2QBF cover-drop"),
        ("out-ganak-mccomp2324-2799164-1", "+dynamic BCE (now)"),
    ]),
}


def times(cur, dirname):
    rows = cur.execute("select ganak_time from data where dirname=? and ganak_time is not null "
                       "and ganak_time < ? order by ganak_time", (dirname, TOUT)).fetchall()
    return [r[0] for r in rows]


def main():
    cur = sqlite3.connect(DB).cursor()
    for name, g in GRAPHS.items():
        plots = []
        for i, (d, title) in enumerate(g["runs"]):
            ts = times(cur, d)
            dat = f"{name}-{i}.dat"
            with open(dat, "w") as f:
                f.write("0 0\n")
                for n, t in enumerate(ts, 1):
                    f.write(f"{t} {n}\n")
            col = COLORS[i] if i < len(g["runs"]) - 1 else COLORS[-1]
            plots.append(f'"{dat}" u 1:2 w l lw 3 lc rgb "{col}" t "{title} ({len(ts)})"')
            print(f"{name}: {title}: {len(ts)}")
        lo, hi = g["yr"]
        gp = f"""set terminal pdfcairo enhanced color font "Helvetica,11" size 6.2in,2.7in
set output "{name}.pdf"
set key outside right center spacing 1.3 samplen 2 invert
set xlabel "Time (s)"
set ylabel "Instances counted (of 1600)"
set grid lc rgb "#dddddd"
set border lc rgb "#555555"
set xrange [{g.get('xr', (0, TOUT))[0]}:{g.get('xr', (0, TOUT))[1]}]
set yrange [{lo}:{hi}]
plot {", ".join(plots)}
"""
        with open(f"{name}.gnuplot", "w") as f:
            f.write(gp)
        subprocess.run(["gnuplot", f"{name}.gnuplot"], check=True)


if __name__ == "__main__":
    main()
