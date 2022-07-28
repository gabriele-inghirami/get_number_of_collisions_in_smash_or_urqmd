It is assumed that a Singularity container with smash (2.2) executable is available.

Index of the files:
- archive_smash.sh slurm script to compress SMASH output data
- config_17_3_timeless.yaml Ecm 17.3, Time_Step_Mode = None
- config_17_3.yaml Ecm 17.3, SMASH defaults
- config_200_timeless.yaml Ecm 200, Time_Step_Mode = None
- config_200.yaml Ecm 200, SMASH defaults
- config_8_7_timeless.yaml Ecm 8.7, Time_Step_Mode = None
- config_8_7.yaml Ecm 9.7, SMASH defaults
- config_powform-1_17_3.yaml Ecm 17.3, Power_Particle_Formation = -1 (no cross section until formation time)
- config_powform-1_8_7.yaml Ecm 8.7, Power_Particle_Formation = -1 (no cross section until formation time)
- launch_runs_smash_powform.sh bash script that launches runs with Power_Particle_Formation = -1
- launch_runs_smash.sh bash script that launches runs with default parameters
- launch_runs_smash_timeless.sh bash script that launches runs with Time_Step_Mode = None
- postproc_smash.sh script that starts the postprocessing, i.e. the analysis of the collision history
- run_smash_pf.bash script executed by launch_runs_smash_powform.sh that starts slurm jobs
- run_smash_timeless.bash script executed by launch_runs_smash_timeless.sh that starts slurm jobs
