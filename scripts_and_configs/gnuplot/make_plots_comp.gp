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


set xrange[-2:40]
set mxtics 10
set mytics 10

dirs="diff_urqmd_smash_std diff_urqmd_smash_-1 diff_smash_std_smash_-1"
titles="'UrQMD - SMASH (PPF +1)' 'UrQMD - SMASH (PPF -1)' 'SMASH (PPF +1) - SMASH (PPF -1)'"

cft="collision_types.dat"
hft="hadron_types.dat"

do for [k=1:words(dirs)] {


set out word(dirs,k)."/Ecm_8_7.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 8.7 GeV, ".word(titles,k)
pf=word(dirs,k)."/8_7/".cft
plot pf u 1:2 w l ls 1 t "elastic", pf u 1:3 w l ls 2 t "decays", pf u 1:4 w l ls 3 t "strings", pf u 1:5 w l ls 4 t "other"

set out word(dirs,k)."/Ecm_17_3.eps"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 17.3 GeV".word(titles,k)
pf=word(dirs,k)."/17_3/".cft
plot pf u 1:2 w l ls 1 t "elastic", pf u 1:3 w l ls 2 t "decays", pf u 1:4 w l ls 3 t "strings", pf u 1:5 w l ls 4 t "other"
}

set ylabel "dN/dt [fm^{-1}]"
set xlabel "t [fm]"
energies="'8_7' '17_3'"
en_labels="'8.7' '17.3'"
names="'two_stable' 'one_stable' 'no_stable' 'min_1_antip' 'two_baryons' 'baryon_meson' 'two_mesons' 'two_nucleons' 'nucleon_pion' 'two_pions' 'NNstar'"
n_labels="'(Mininum) 2 stable particles' '(Mininum) 1 stable particle' 'No stable particles' '(Minimum) 1 antiparticle' '(Minimum) 2 baryons' '(Minimum) 1 baryon and 1 meson' '(Minimum) 2 mesons' '(Minimum) 2 nucleons' '(Minimum) 1 nucleon and 1 pion' '(Minimum) 2 pions' '(Min.) 1 nucleon and 1 excited nucleon'"
do for [en=1:2] {
   u_ss=word(dirs,1)."/".word(energies,en)."/hadron_types.dat"
   u_sm=word(dirs,2)."/".word(energies,en)."/hadron_types.dat"
   ss_sm=word(dirs,3)."/".word(energies,en)."/hadron_types.dat"
   do for [kn=1:words(names)] {
      set out "Ecm_".word(energies,en)."_".word(names,kn).".eps"
      set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = ".word(en_labels,en).", ".word(n_labels,kn)
      indx=kn+1
      plot u_ss u 1:indx w l lw 4 lc "red" dt 1 t word(titles,1), u_sm u 1:indx w l lw 4 lc "blue" dt 2 t word(titles,2), ss_sm u 1:indx w l lw 4 lc "web-green" dt 3 t word(titles,3)
   }
}
