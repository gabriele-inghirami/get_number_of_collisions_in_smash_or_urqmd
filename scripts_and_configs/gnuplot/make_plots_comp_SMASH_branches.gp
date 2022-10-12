set term pngcairo dashed font "Times, 22" size 1200,800

set key top right Left font ",14"

set ls 1 lc "red" lw 4 dt 1
set ls 2 lc "orange" lw 4 dt 1
set ls 3 lc "turquoise" lw 4 dt 1
set ls 4 lc "web-green" lw 4 dt 1
set ls 5 lc "red" lw 4 dt 2
set ls 6 lc "orange" lw 4 dt 2
set ls 7 lc "turquoise" lw 4 dt 2
set ls 8 lc "web-green" lw 4 dt 2

AA="2.2.1"
BB="Justin"

lb="AA.' elastic' AA.' decays' AA.' strings' AA.' other' BB.' elastic' BB.' decays' BB.' strings' BB.' other'"

set xrange[0.:19]
set xtics 2
set mxtics 4
set mytics 2
set key top right

AAdir="./"
BBdir="./"

AA19dir=AAdir."19_6_std/"
BB19dir=BBdir."19_6_jm/"
AA200dir=AAdir."200_std/"
BB200dir=BBdir."200_jm/"
AA2760dir=AAdir."2760_std/"
BB2760dir=BBdir."2760_jm/"

cf="collision_types.dat"
pf="process_types.dat"
hf="hadron_types.dat"

set xlabel "time [fm]"
set ylabel "dN/dt [fm^{-1}]"

set out "Ecm_19_6.png"
set title "Au+Au, b = 0-3.3 fm, {/Symbol \326}s = 19.6 GeV"
sf=AA19dir.cf
uf=BB19dir.cf
plot sf u 1:2 w l ls 1 t AA." elastic", sf u 1:3 w l ls 2 t AA." decays", sf u 1:4 w l ls 3 t AA." strings", sf u 1:5 w l ls 4 t AA." other", uf u 1:2 w l ls 5 t BB." elastic", uf u 1:3 w l ls 6 t BB." decays", uf u 1:4 w l ls 7 t BB." strings", uf u 1:5 w l ls 8 t BB." other"

set out "Ecm_200.png"
set title "Au+Au, b = 0-3.3 fm, {/Symbol \326}s = 200 GeV"
sf=AA200dir.cf
uf=BB200dir.cf
plot sf u 1:2 w l ls 1 t AA." elastic", sf u 1:3 w l ls 2 t AA." decays", sf u 1:4 w l ls 3 t AA." strings", sf u 1:5 w l ls 4 t AA." other", uf u 1:2 w l ls 5 t BB." elastic", uf u 1:3 w l ls 6 t BB." decays", uf u 1:4 w l ls 7 t BB." strings", uf u 1:5 w l ls 8 t BB." other"

set out "Ecm_2760.png"
set title "Pb+Pb, b = 0-3.3 fm, {/Symbol \326}s = 2760 GeV"
sf=AA2760dir.cf
uf=BB2760dir.cf
plot sf u 1:2 w l ls 1 t AA." elastic", sf u 1:3 w l ls 2 t AA." decays", sf u 1:4 w l ls 3 t AA." strings", sf u 1:5 w l ls 4 t AA." other", uf u 1:2 w l ls 5 t BB." elastic", uf u 1:3 w l ls 6 t BB." decays", uf u 1:4 w l ls 7 t BB." strings", uf u 1:5 w l ls 8 t BB." other"

energies="'19_6' '200' '2760'"
en_labels="'19.6' '200' '2760'"
species="'Au+Au' 'Au+Au' 'Pb+Pb'"
names="'two_stable' 'one_stable' 'no_stable' 'min_1_antip' 'two_baryons' 'baryon_meson' 'two_mesons' 'two_nucleons' 'nucleon_pion' 'two_pions' 'NNstar'"
n_labels="'(Mininum) 2 stable particles' '(Mininum) 1 stable particle' 'No stable particles' '(Minimum) 1 antiparticle' '(Minimum) 2 baryons' '(Minimum) 1 baryon and 1 meson' '(Minimum) 2 mesons' '(Minimum) 2 nucleons' '(Minimum) 1 nucleon and 1 pion' '(Minimum) 2 pions' '(Min.) 1 nucleon and 1 excited nucleon'"
do for [en=1:3] {
   sf=AAdir.word(energies,en)."_std/hadron_types.dat"
   uf=BBdir.word(energies,en)."_jm/hadron_types.dat"
   do for [kn=1:words(names)] {
      set out "Ecm_".word(energies,en)."_".word(names,kn).".png"
      set title word(species,en).", b = 0-3.3 fm, {/Symbol \326}s = ".word(en_labels,en).", ".word(n_labels,kn)
      indx=kn+1
      plot sf u 1:indx w l lw 4 lc "red" dt 1 t AA, uf u 1:indx w l lw 4 lc "blue" dt 2 t BB
   }
}
