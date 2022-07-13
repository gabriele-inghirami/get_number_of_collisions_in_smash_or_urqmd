set term pos eps enh col font "Times, 22"

set key top right Left font ",14"

set ls 1 lc "red" lw 4 dt 1
set ls 2 lc "orange" lw 4 dt 1
set ls 3 lc "turquoise" lw 4 dt 1
set ls 4 lc "web-green" lw 4 dt 1
set ls 5 lc "magenta" lw 4 dt 4
set ls 6 lc "coral" lw 4 dt 4
set ls 7 lc "purple" lw 4 dt 4
set ls 8 lc "sea-green" lw 4 dt 4


lb="'SMASH elastic' 'SMASH decays' 'SMASH strings' 'SMASH other' 'UrQMD elastic' 'UrQMD decays' 'UrQMD strings' 'UrQMD other'"

set logscale y
set xrange[-3.5:200.5]
set yrange [0.001:3000]
set mxtics 10

set out "Ecm_8_7_ylog.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV"
sf="../smash_runs2/smash_8_7.dat"
uf="../urqmd_runs2/urqmd_8_7.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_17_3_ylog.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV"
sf="../smash_runs2/smash_17_3.dat"
uf="../urqmd_runs2/urqmd_17_3.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_200_ylog.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
sf="../smash_runs2/smash_200.dat"
uf="../urqmd_runs2/urqmd_200.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"


unset logscale y

set ls 1 lc "red" lw 4 dt 1
set ls 2 lc "purple" lw 4 dt 1
set ls 3 lc "turquoise" lw 4 dt 1
set ls 4 lc "web-green" lw 4 dt 1
set ls 5 lc "red" lw 4 dt 2
set ls 6 lc "purple" lw 4 dt 2
set ls 7 lc "turquoise" lw 4 dt 2
set ls 8 lc "web-green" lw 4 dt 2


lb="'SMASH elastic' 'SMASH decays' 'SMASH strings' 'SMASH other' 'UrQMD elastic' 'UrQMD decays' 'UrQMD strings' 'UrQMD other'"

set xrange[-3.5:200.5]
set mxtics 10

set out "Ecm_8_7.eps"
set yrange [0.001:250]
set xrange [-3:100]
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV"
sf="../smash_runs2/smash_8_7.dat"
uf="../urqmd_runs2/urqmd_8_7.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_17_3.eps"
set yrange [0.001:400]
set xrange [-3:100]
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV"
sf="../smash_runs2/smash_17_3.dat"
uf="../urqmd_runs2/urqmd_17_3.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_200.eps"
set yrange [0.001:1000]
set xrange [-3:150]
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
sf="../smash_runs2/smash_200.dat"
uf="../urqmd_runs2/urqmd_200.dat"
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set logscale y
set xrange[-3.5:200.5]
set yrange [0.001:3000]
set mxtics 10

set ls 9 lc "blue" lw 4 dt 2

set out "Ecm_8_7_ylog_total.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV"
sf="../smash_runs2/smash_8_7.dat"
uf="../urqmd_runs2/urqmd_8_7.dat"
plot sf u 1:(($2)+($3)+($4)+($5)) w l ls 1 t "SMASH total", uf u 1:(($2)+($3)+($4)+($5)) w l ls 9 t "UrQMD total"

set out "Ecm_17_3_ylog_total.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV"
sf="../smash_runs2/smash_17_3.dat"
uf="../urqmd_runs2/urqmd_17_3.dat"
plot sf u 1:(($2)+($3)+($4)+($5)) w l ls 1 t "SMASH total", uf u 1:(($2)+($3)+($4)+($5)) w l ls 9 t "UrQMD total"

set out "Ecm_200_ylog_total.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
sf="../smash_runs2/smash_200.dat"
uf="../urqmd_runs2/urqmd_200.dat"
plot sf u 1:(($2)+($3)+($4)+($5)) w l ls 1 t "SMASH total", uf u 1:(($2)+($3)+($4)+($5)) w l ls 9 t "UrQMD total"

