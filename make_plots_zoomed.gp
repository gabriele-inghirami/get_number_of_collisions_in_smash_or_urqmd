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

sdir="../smash_all_data/"
udir="../urqmd_all_data/"

s8dir=sdir."8_7/"
s17dir=sdir."17_3/"
s200dir=sdir."200/"
u8dir=udir."8_7/"
u17dir=udir."17_3/"
u200dir=udir."200/"

cf="collision_types.dat"
pf="process_types.dat"
hf="hadron_types.dat"

set out "Ecm_8_7.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV"
sf=s8dir.cf
uf=u8dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_17_3.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV"
sf=s17dir.cf
uf=u17dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set out "Ecm_200.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
sf=s200dir.cf
uf=u200dir.cf
plot sf u 1:2 w l ls 1 t "SMASH elastic", sf u 1:3 w l ls 2 t "SMASH decays", sf u 1:4 w l ls 3 t "SMASH strings", sf u 1:5 w l ls 4 t "SMASH other", uf u 1:2 w l ls 5 t "UrQMD elastic", uf u 1:3 w l ls 6 t "UrQMD decays", uf u 1:4 w l ls 7 t "UrQMD strings", uf u 1:5 w l ls 8 t "UrQMD other"

set ylabel "dN/dt [fm^{-1}]"
set xlabel "t [fm]"
energies="'8_7' '17_3' '200'"
en_labels="'8.7' '17.3' '200'"
names="'two_stable' 'one_stable' 'no_stable' 'min_1_antip' 'two_baryons' 'baryon_meson' 'two_mesons' 'two_nucleons' 'nucleon_pion' 'two_pions' 'NNstar'"
n_labels="'(Mininum) 2 stable particles' '(Mininum) 1 stable particle' 'No stable particles' '(Minimum) 1 antiparticle' '(Minimum) 2 baryons' '(Minimum) 1 baryon and 1 meson' '(Minimum) 2 mesons' '(Minimum) 2 nucleons' '(Minimum) 1 nucleon and 1 pion' '(Minimum) 2 pions' '(Min.) 1 nucleon and 1 excited nucleon'"
do for [en=1:3] {
   sf=sdir.word(energies,en)."/hadron_types.dat"
   uf=udir.word(energies,en)."/hadron_types.dat"
   do for [kn=1:words(names)] {
      set out "Ecm_".word(energies,en)."_".word(names,kn).".eps"
      set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = ".word(en_labels,en).", ".word(n_labels,kn)
      indx=kn+1
      plot sf u 1:indx w l lw 4 lc "red" dt 1 t "SMASH 2.2", uf u 1:indx w l lw 4 lc "blue" dt 2 t "UrQMD 3.4"
   }
}
