#for h in A B C D E F G H I L 
for h in A B C D E F G H I L M N O P
do
sbatch --job-name=urqmd_8_7_$h run.bash 8_7 $h
sbatch --job-name=urqmd_17_3_$h run.bash 17_3 $h
sbatch --job-name=urqmd_200_$h run.bash 200 $h
done
