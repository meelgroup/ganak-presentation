set terminal pdfcairo enhanced color font "Helvetica,11" size 6.2in,2.7in
set output "cav-versions.pdf"
set key outside right center spacing 1.3 samplen 2
set xlabel "Time (s)"
set ylabel "Instances counted (of 1600)"
set grid lc rgb "#dddddd"
set border lc rgb "#555555"
set xrange [0:3600]
set yrange [700:1140]
plot "cav-versions-0.dat" u 1:2 w l lw 3 lc rgb "#7f7f7f" t "Ganak (2019) (778)", "cav-versions-1.dat" u 1:2 w l lw 3 lc rgb "#1f77b4" t "+ChronoBT +SAT (906)", "cav-versions-2.dat" u 1:2 w l lw 3 lc rgb "#2ca02c" t "+enhanced SAT (924)", "cav-versions-3.dat" u 1:2 w l lw 3 lc rgb "#9467bd" t "+dual indep. set (1071)", "cav-versions-4.dat" u 1:2 w l lw 3 lc rgb "#d62728" t "Ganak2 (CAV'25) (1121)"
