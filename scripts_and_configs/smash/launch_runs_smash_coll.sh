for h in A B C D E F G H I J K L M N O P Q R S T #U V X Y Z
do
sbatch --job-name=smash_19_6_$h run_smash_coll.bash 19_6 $h config_coll_Au_19_6.yaml
sbatch --job-name=smash_200_$h run_smash_coll.bash 200 $h config_coll_Au_200.yaml
sbatch --job-name=smash_2760_$h run_smash_coll.bash 2760 $h config_coll_Pb_2760.yaml
done
