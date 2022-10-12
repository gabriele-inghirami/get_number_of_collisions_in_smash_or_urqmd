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
##SBATCH --mail-user= INSERT YOUR EMAIL and UNCOMMENT if you wish to get informed by email

#Syntax: sbatch --job-name=<name of the job> run_urqmd.bash <suffix of the desired config file> <additional label for multiple runs>
#Syntax example: sbatch bash --job-name=urqmd_17_3 run_urqmd.bash 17_3 A

iterations=1

workdir=$LH/collisions_urqmd/

udir=$workdir/urqmd-3.4

rundir=$workdir/$SLURM_JOB_NAME$2

ion_run=inputfile_$1

if [ ! -d $rundir ]
then
    cp -R $udir $rundir
    cd $rundir
    if [ $3 == LHC ]
    then
       make lhc
       urqmd_exe=urqmd.$(uname -m).lhc 
    else
       make
       urqmd_exe=urqmd.$(uname -m) 
    fi
fi

mkdir -p $workdir/random_numbers_dir

function check_rnd () {
  n_items=$(ls $workdir/random_numbers_dir | grep $1 | wc -l)
  if [ $n_items != 1 ]
  then
     touch $workdir/random_numbers_dir/$1
     echo 1
  else
     echo 0
  fi
}


for k in $(seq 1 $iterations)
do
    for i in $(seq 1 $SLURM_NTASKS)
    do
        rnds=$(tr -cd "[:digit:]" < /dev/urandom | head -c 8)
        echo "Trying with random number " $rnds
        while [ $(check_rnd $rnds) == 0 ]
        do
            echo $rnds " already used"
            rnds=$(tr -cd "[:digit:]" < /dev/urandom | head -c 8)
            echo "Trying again with random number " $rnds
        done

        infile=$rundir/in_$i\_$k
        cp $workdir/$ion_run $infile

        sed -i -e "s/rsd 0/rsd $rnds/" $infile

        export ftn09=$infile
        export ftn15=$rundir/out_$i\_$k.f15

        ./$urqmd_exe &
    done
    wait
done
sleep 60
