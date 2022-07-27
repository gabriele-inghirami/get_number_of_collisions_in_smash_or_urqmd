for h in A B C D E F G H I L
do
sbatch --job-name=smash_8_7_$h run_smash.bash 8_7 $h
sbatch --job-name=smash_17_3_$h run_smash.bash 17_3 $h
sbatch --job-name=smash_200_$h run_smash.bash 200 $h
done
