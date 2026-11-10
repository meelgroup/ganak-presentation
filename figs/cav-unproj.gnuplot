set terminal pdfcairo enhanced color font "Helvetica,11" size 6.2in,2.7in
set output "cav-unproj.pdf"
set key outside right center spacing 1.3 samplen 2 invert
set xlabel "Time (s)"
set ylabel "Instances counted (of 800)"
set grid lc rgb "#dddddd"
set border lc rgb "#555555"
set xrange [0:3600]
set yrange [350:560]
plot "cav-unproj-0.dat" u 1:2 w l lw 3 lc rgb "#7f7f7f" t "Ganak (2019) (391)", "cav-unproj-1.dat" u 1:2 w l lw 3 lc rgb "#1f77b4" t "gpmc (421)", "cav-unproj-2.dat" u 1:2 w l lw 3 lc rgb "#2ca02c" t "d4 (514)", "cav-unproj-3.dat" u 1:2 w l lw 3 lc rgb "#9467bd" t "SharpSAT-TD (523)", "cav-unproj-4.dat" u 1:2 w l lw 3 lc rgb "#d62728" t "Ganak2 (CAV'25) (550)"
