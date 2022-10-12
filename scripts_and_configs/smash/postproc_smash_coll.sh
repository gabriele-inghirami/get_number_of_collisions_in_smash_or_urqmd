#!/usr/bin/bash
#SBATCH --job-name=postproc_smash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
##SBATCH --nodes=1
#SBATCH --ntasks=60
#SBATCH --mem-per-cpu=2G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-2:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

container=$LH/smash-2.2-jammy_2022.10.07.sif

datadir=$LH/collisions_smash/

for i in {1..10}
do
singularity exec $container python3 get_number_of_collisions.py smash_coll_2760_p$i.pickle  "Pb-Pb, Ecm = 2.76 TeV, b = 0-3.3 fm, SMASH 2.2.1" $datadir/out_2760_*$i\_1/full_event_history.oscar &> log2.76$i &
singularity exec $container python3 get_number_of_collisions.py smash_coll_19_6_p$i.pickle  "Au-Au, Ecm = 19.6 GeV, b = 0-3.3 fm, SMASH 2.2.1" $datadir/out_19_6_*$i\_1/full_event_history.oscar &> log19.6$i &
singularity exec $container python3 get_number_of_collisions.py smash_coll_200_p$i.pickle  "Au-Au, Ecm = 200 GeV, b = 0-3.3 fm, SMASH 2.2.1" $datadir/out_200_*$i\_1/full_event_history.oscar &> log200$i &
done

for i in {1..10}
do
singularity exec $container python3 get_number_of_collisions.py smash_coll_2760_jm_p$i.pickle  "Pb-Pb, Ecm = 2.76 TeV, b = 0-3.3 fm, SMASH Justin" $datadir/run_dev_2760*/out_$i\_1/full_event_history.oscar &> logjm2.76$i &
singularity exec $container python3 get_number_of_collisions.py smash_coll_19_6_jm_p$i.pickle  "Au-Au, Ecm = 19.6 GeV, b = 0-3.3 fm, SMASH Justin" $datadir/run_dev_19_6*/out_$i\_1/full_event_history.oscar &> logjm19.6$i &
singularity exec $container python3 get_number_of_collisions.py smash_coll_200_jm_p$i.pickle  "Au-Au, Ecm = 200 GeV, b = 0-3.3 fm, SMASH Justin" $datadir/run_dev_200*/out_$i\_1/full_event_history.oscar &> logjm200$i &
done
wait
sleep 60
