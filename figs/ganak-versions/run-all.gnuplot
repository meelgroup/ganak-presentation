set term postscript eps color lw 1 "Helvetica" 15 size 3.4,2
set output "run.eps"
set title
set key bottom right
unset logscale x
unset logscale y
set title "All instances"
unset title
set ylabel  "Instances counted"
set xlabel "Time (s)"
unset ylabel
set style line 1 lt 1 lc rgb "red" pointsize 0.7 lw 2 pt 1
set style line 2 lt 2 lc rgb "blue" pointsize 0.7 lw 2 pt 2
set style line 3 lt 3 lc rgb "dark-green" pointsize 0.7 lw 2 pt 3
set style line 4 lt 4 lc rgb "purple" pointsize 0.7 lw 2 pt 4
set style line 5 lt 5 lc rgb "orange" pointsize 0.7 lw 2 pt 5
set style line 6 lt 6 lc rgb "magenta" pointsize 0.7 lw 2 pt 6
set style line 7 lt 7 lc rgb "black" pointsize 0.7 lw 2 pt 7
set style line 8 lt 8 lc rgb "gold" pointsize 0.7 lw 2 pt 8
plot [:3600][400:]\
"run-out-ganak-mc2324-14063135-1.csv.gnuplotdata" u 2:1 with linespoints ls 1 title "Ganak",\
"run-out-ganak-mc2324-14072353-1.csv.gnuplotdata" u 2:1 with linespoints ls 7 title "Ganak+CB+SAT",\
"run-out-ganak-mc2324-14063135-7.csv.gnuplotdata" u 2:1 with linespoints ls 6 title "Ganak+CB+SAT+enhanceSAT",\
"run-out-ganak-mc2324-14063135-4.csv.gnuplotdata" u 2:1 with linespoints ls 8 title "Ganak+CB+SAT+enhanceSAT+DualSet",\
"run-out-ganak-mc2324-14063135-0.csv.gnuplotdata" u 2:1 with linespoints ls 5 title "Ganak+All = Ganak2"
