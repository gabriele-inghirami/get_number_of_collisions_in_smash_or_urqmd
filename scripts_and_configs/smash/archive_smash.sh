#!/usr/bin/bash
#SBATCH --job-name=archive_smash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=3
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-7:00:00
##SBATCH --mail-type=ALL
##SBATCH --mail-user=UNCOMMENT AND WRITE YOUR EMAIL ADDRESS HERE IF YOU WANT BE NOTIFIED BY EMAIL

container=$LH/smash-2.2-jammy.sif

singularity exec $container zip -r smas_8_7.zip out_8* &> log8 &
singularity exec $container zip -r smas_17_3.zip out_17* &> log17 &
singularity exec $container zip -r smas_200.zip out_200* &> log200 &
wait
sleep 60
