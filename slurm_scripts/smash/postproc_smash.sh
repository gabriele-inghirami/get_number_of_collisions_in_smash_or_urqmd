#!/usr/bin/bash
#SBATCH --job-name=postproc_smash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=30
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-7:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

container=$LH/smash-2.2-jammy.sif

for i in {1..10}
do
singularity exec $container python3 get_number_of_collisions.py smash8_7_p$i.pickle  "Au-Au, Ecm = 8.7 GeV, b = 0-3.3 fm, SMASH" out_8_7*$i\_1/full_event_history.oscar &> log8$i &
singularity exec $container python3 get_number_of_collisions.py smash17_p$i.pickle  "Au-Au, Ecm = 17.3 GeV, b = 0-3.3 fm, SMASH" out_17_3*$i\_1/full_event_history.oscar &> log17$i &
singularity exec $container python3 get_number_of_collisions.py smash200_p$i.pickle  "Au-Au, Ecm = 200 GeV, b = 0-3.3 fm, SMASH" out_200_*$i\_1/full_event_history.oscar &> log200$i &
done
wait
sleep 60
