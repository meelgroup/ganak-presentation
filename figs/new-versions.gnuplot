set terminal pdfcairo enhanced color font "Helvetica,11" size 6.2in,2.7in
set output "new-versions.pdf"
set key outside right center spacing 1.3 samplen 2
set xlabel "Time (s)"
set ylabel "Instances counted (of 1600)"
set grid lc rgb "#dddddd"
set border lc rgb "#555555"
set xrange [0:3600]
set yrange [1100:1225]
plot "new-versions-0.dat" u 1:2 w l lw 3 lc rgb "#7f7f7f" t "Jun 2026 baseline (1181)", "new-versions-1.dat" u 1:2 w l lw 3 lc rgb "#1f77b4" t "+new TD selection (1198)", "new-versions-2.dat" u 1:2 w l lw 3 lc rgb "#2ca02c" t "+TD flat/dense rules (1205)", "new-versions-3.dat" u 1:2 w l lw 3 lc rgb "#9467bd" t "+2QBF cover-drop (1210)", "new-versions-4.dat" u 1:2 w l lw 3 lc rgb "#d62728" t "+dynamic BCE (now) (1220)"
