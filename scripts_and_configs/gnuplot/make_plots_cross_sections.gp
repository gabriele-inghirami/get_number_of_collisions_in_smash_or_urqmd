set term pos eps enh col font "Times, 22"

set key top right Left font ",14"

set ls 1 lc "red" lw 4 dt 1
set ls 2 lc "orange" lw 4 dt 1
set ls 3 lc "turquoise" lw 4 dt 1
set ls 4 lc "web-green" lw 4 dt 1
set ls 5 lc "red" lw 4 dt 2
set ls 6 lc "orange" lw 4 dt 2
set ls 7 lc "turquoise" lw 4 dt 2
set ls 8 lc "web-green" lw 4 dt 2


lb="'SMASH elastic' 'SMASH decays' 'SMASH strings' 'SMASH other' 'UrQMD elastic' 'UrQMD decays' 'UrQMD strings' 'UrQMD other'"

set xrange[0.:20]
set mxtics 4
set key top right

sdir="../smash_cross_sections/"
udir="../urqmd_cross_sections/"

s8dir=sdir."8_7/"
s17dir=sdir."17_3/"
s200dir=sdir."200/"
u8dir=udir."8_7/"
u17dir=udir."17_3/"
u200dir=udir."200/"

cf="cross_sections.dat"
ef="average_collision_energies.dat"
hn="average_created_hadrons.dat"


# total cross sections

set xlabel "t [fm]"
set ylabel "{/Symbol s} [mb]"

set out "Ecm_8_7_total_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV, total cross sections"
sf=s8dir.cf
uf=u8dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_17_3_total_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV, total cross sections"
sf=s17dir.cf
uf=u17dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_200_total_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV, total cross sections"
sf=s200dir.cf
uf=u200dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"


# partial cross sections

set out "Ecm_8_7_partial_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV, partial cross sections"
sf=s8dir.cf
uf=u8dir.cf
plot sf u 1:6 w l ls 1 t "SMASH elastic", sf u 1:7 w l ls 2 t "SMASH decays", sf u 1:8 w l ls 3 t "SMASH strings", sf u 1:9 w l ls 4 t "SMASH other", uf u 1:6 w l ls 5 t "UrQMD elastic", uf u 1:7 w l ls 6 t "UrQMD decays", uf u 1:8 w l ls 7 t "UrQMD strings", uf u 1:9 w l ls 8 t "UrQMD other"

set out "Ecm_17_3_partial_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV, partial cross sections"
sf=s17dir.cf
uf=u17dir.cf
plot sf u 1:6 w l ls 1 t "SMASH elastic", sf u 1:7 w l ls 2 t "SMASH decays", sf u 1:8 w l ls 3 t "SMASH strings", sf u 1:9 w l ls 4 t "SMASH other", uf u 1:6 w l ls 5 t "UrQMD elastic", uf u 1:7 w l ls 6 t "UrQMD decays", uf u 1:8 w l ls 7 t "UrQMD strings", uf u 1:9 w l ls 8 t "UrQMD other"

set out "Ecm_200_partial_cross_sections.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV, partial cross sections"
sf=s200dir.cf
uf=u200dir.cf
plot sf u 1:6 w l ls 1 t "SMASH elastic", sf u 1:7 w l ls 2 t "SMASH decays", sf u 1:8 w l ls 3 t "SMASH strings", sf u 1:9 w l ls 4 t "SMASH other", uf u 1:6 w l ls 5 t "UrQMD elastic", uf u 1:7 w l ls 6 t "UrQMD decays", uf u 1:8 w l ls 7 t "UrQMD strings", uf u 1:9 w l ls 8 t "UrQMD other"

# average collision energies

set ylabel "<{/Symbol \326}s> [Gev]"

set out "Ecm_8_7_collision_energy.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV, average collision energy"
sf=s8dir.ef
uf=u8dir.ef
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_17_3_collision_energy.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV, average collision energy"
sf=s17dir.ef
uf=u17dir.ef
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_200_collision_energy.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV, average collision energy"
sf=s200dir.ef
uf=u200dir.ef
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

# average number of hadrons

set ylabel "<# created hadrons>"

set out "Ecm_8_7_created hadrons.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV, additional hadrons wrt in. nucl."
sf=s8dir.hn
uf=u8dir.hn
plot sf u 1:2 w l ls 1 t "SMASH", uf u 1:2 w l ls 5 t "UrQMD"

set out "Ecm_17_3_created_hadrons.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV, additional hadrons wrt in. nucl."
sf=s17dir.hn
uf=u17dir.hn
plot sf u 1:2 w l ls 1 t "SMASH", uf u 1:2 w l ls 5 t "UrQMD"

set out "Ecm_200_created_hadrons.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV, additional hadrons wrt in. nucl."
sf=s200dir.hn
uf=u200dir.hn
plot sf u 1:2 w l ls 1 t "SMASH", uf u 1:2 w l ls 5 t "UrQMD"
