#!/usr/bin/bash
#SBATCH --job-name=coll_stat
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-7:00:00
##SBATCH --mail-type=ALL
##SBATCH --mail-user=UNCOMMENT AND WRITE YOUR EMAIL ADDRESS HERE IF YOU WANT BE NOTIFIED BY EMAIL

#Syntax: sbatch --job-name=<name of the job> run_smash.bash <suffix of the desired config file> <additional label for multiple runs>
#Syntax example: sbatch --job-name=smash_17_3 run_smash.bash 17_3 A

iterations=1

container=$LH/smash_2.2-wgcc8.sif

for k in $(seq 1 $iterations)
do
    for i in $(seq 1 $SLURM_NTASKS)
    do
        singularity exec $container smash -i config_powform-1_$1.yaml -o out_$1\_$2\_$i\_$k &> log_$1\_$2\_$i\_$k &
    done
    wait
done
sleep 20
