for h in A B C D E F G H I L
do
sbatch --job-name=urqmd_8_7_$h run_urqmd.bash 8_7 $h
sbatch --job-name=urqmd_17_3_$h run_urqmd.bash 17_3 $h
sbatch --job-name=urqmd_200_$h run_urqmd.bash 200 $h
done
