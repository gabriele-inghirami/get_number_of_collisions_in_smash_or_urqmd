for h in A B C D E F G H I J K L M N O P Q R S T U V X Y Z
do
sbatch --job-name=smash_8_7_$h run_smash_pf.bash 8_7 $h
sbatch --job-name=smash_17_3_$h run_smash_pf.bash 17_3 $h
done
