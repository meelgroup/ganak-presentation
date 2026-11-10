#!/usr/bin/env python3
# Primal graph (coloured by TD score) + tree decomposition of td-example.cnf. Usage: cd figs/td && ./make_td.py
import os
import re
import subprocess
import tempfile
from itertools import combinations

TREEDECOMP = os.environ.get("TREEDECOMP", "../../../../treedecomp/build/treedecomp")
CNF = "td-example.cnf"
FONT = "Latin Modern Sans"
# score -> (fill, border); same palette as the slides: orange = centroid, blue, grey
STYLE = {100: ("#fbeedd", "#e18c2b"), 50: ("#e8eef6", "#4673aa"), 0: ("#eeeeee", "#777777")}


def run_td():
    out = subprocess.run([TREEDECOMP, "--tdvis", "raw-td.dot", CNF],
                         capture_output=True, text=True, check=True).stdout
    scores = {int(v): int(s) for v, s in re.findall(r"^(\d+) (\d+)$", out, re.M)}
    dot = open("raw-td.dot").read()
    os.remove("raw-td.dot")
    bags = {int(b): [int(x) for x in vs.split(", ")]
            for b, vs in re.findall(r"b(\d+) \[label=\"bag \d+[^{]*\{([^}]*)\}", dot)}
    m = re.search(r"b(\d+) \[label=\"bag \d+ \(centroid\)", dot)
    assert m, "treedecomp did not mark a centroid bag"
    centroid = int(m.group(1))
    edges = [(int(a), int(b)) for a, b in re.findall(r"b(\d+) -- b(\d+)", dot)]
    return scores, bags, centroid, edges


def primal_edges():
    es = set()
    for line in open(CNF):
        if line.startswith(("c", "p")) or not line.strip():
            continue
        vs = sorted({abs(int(x)) for x in line.split()[:-1]})
        es.update(combinations(vs, 2))
    return sorted(es)


def node_attrs(score):
    fill, border = STYLE[score]
    return f'style=filled, fillcolor="{fill}", color="{border}", penwidth=1.6'


def main():
    scores, bags, centroid, edges = run_td()
    common = f'fontname="{FONT}", fontsize=16'
    with open("primal.dot", "w") as f:
        f.write(f"graph P {{\n  layout=neato; overlap=false; sep=0.4;\n"
                f"  node [shape=circle, width=0.6, fixedsize=true, fontname=\"{FONT}\", fontsize=24];\n  edge [color=\"#888888\"];\n")
        for v, s in sorted(scores.items()):
            f.write(f'  {v} [label="{v}", {node_attrs(s)}];\n')
        for a, b in primal_edges():
            f.write(f"  {a} -- {b};\n")
        f.write("}\n")
    with open("tree.dot", "w") as f:
        f.write(f"graph T {{\n  node [shape=box, style=\"rounded,filled\", {common}];\n  edge [color=\"#555555\"];\n")
        adj = {b: [] for b in bags}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        depth, todo, tree = {centroid: 0}, [centroid], []
        while todo:
            u = todo.pop(0)
            for w in adj[u]:
                if w not in depth:
                    depth[w] = depth[u] + 1
                    todo.append(w)
                    tree.append((u, w))
        for b, vs in sorted(bags.items()):
            fill, border = STYLE[{0: 100, 1: 50}.get(depth[b], 0)]
            pw = 3 if b == centroid else 1.4
            f.write(f'  b{b} [label="{{{", ".join(map(str, vs))}}}", fillcolor="{fill}", color="{border}", penwidth={pw}];\n')
        for u, w in tree:
            f.write(f"  b{u} -- b{w};\n")
        f.write("}\n")
    with tempfile.TemporaryDirectory() as tmp:
        lm = os.path.dirname(subprocess.run(["kpsewhich", "lmsans10-regular.otf"],
                                            capture_output=True, text=True, check=True).stdout.strip())
        conf = os.path.join(tmp, "fonts.conf")
        with open(conf, "w") as c:
            c.write(f'<?xml version="1.0"?><fontconfig><include ignore_missing="yes">/etc/fonts/fonts.conf</include>'
                    f"<dir>{lm}</dir><cachedir>{tmp}/cache</cachedir></fontconfig>")
        env = dict(os.environ, FONTCONFIG_FILE=conf)
        for name in ("primal", "tree"):
            subprocess.run(["dot", "-Tpdf", f"{name}.dot", "-o", f"{name}.pdf"], env=env, check=True)
    print("scores:", scores, "centroid bag:", bags[centroid])


if __name__ == "__main__":
    main()
