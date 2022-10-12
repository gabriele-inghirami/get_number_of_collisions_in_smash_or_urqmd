set term pos eps enh col font "Times, 22"

#set key top right Left font ",14"

set ls 1 lc "red" lw 4 dt 1

set mxtics 5
set mytics 5

set xrange [0:4.9]

sdir="../reduction_factor_urmqd_200/"

s200f=sdir."reduction_factor_200.dat"

set ylabel "Reduction factor"
set xlabel "time [fm]"

set out "Ecm_200_urqmd_reduction_factor.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
plot s200f u 1:2 w l ls 1 notitle
