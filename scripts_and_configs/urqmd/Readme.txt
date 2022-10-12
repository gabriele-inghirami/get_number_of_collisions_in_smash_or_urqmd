It is assumed that a directoy urqmd-3.4 with urqmd source exists in the same directory.
These scipts are replacements of previous scripts used in production runs, but deleted by mistake. 
They should work, but they have not been tested, so a few fixes might be necessary.


Index of the files:
- archive_urqmd.sh slurm script to compress UrQMD output data
- inputfile_17_3, inputfile_200, inputfile_8_7 config files
- 
- launch_runs_urqmd.sh bash script that uses run_urqmd.bash to start the simulations
- postproc_urqmd.sh slurm sbatch script to postprocess the results with get_number_of_collisions.py
- Readme.txt
- run_urqmd.bash sbatch slurm scripts that starts the job, called by launch_runs_urqmd.sh
