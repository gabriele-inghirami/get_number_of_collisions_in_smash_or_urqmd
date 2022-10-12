It is assumed that a Singularity container with smash (2.2) executable is available.

Index of the files:
- archive_smash.sh slurm script to compress SMASH output data
- config_17_3_timeless.yaml Ecm 17.3, Time_Step_Mode = None
- config_17_3.yaml Ecm 17.3, SMASH defaults
- config_200_timeless.yaml Ecm 200, Time_Step_Mode = None
- config_200.yaml Ecm 200, SMASH defaults
- config_200_fragment.yaml  Ecm 200, Separate_Fragment_Baryon: False
- config_8_7_timeless.yaml Ecm 8.7, Time_Step_Mode = None
- config_8_7.yaml Ecm 9.7, SMASH defaults
- config_powform-1_17_3.yaml Ecm 17.3, Power_Particle_Formation = -1 (no cross section until formation time)
- config_powform-1_8_7.yaml Ecm 8.7, Power_Particle_Formation = -1 (no cross section until formation time)
- config_coll_Au_19_6.yaml, config_coll_Au_200.yaml, config_coll_Pb_2760.yaml: to compare version 2.2.1 and J.M.'s branch
- launch_runs_smash_powform.sh bash script that launches runs with Power_Particle_Formation = -1
- launch_runs_smash.sh bash script that launches runs with default parameters
- launch_runs_smash_fragment.sh bash script that launches runs (only 200 GeV) with Separate_Fragment_Baryon: False
- launch_runs_smash_timeless.sh bash script that launches runs with Time_Step_Mode = None
- launch_runs_smash_coll.sh bash script that launches runs to compare version 2.2.1 and J.M.'s branch
- postproc_smash.sh script that starts the postprocessing, i.e. the analysis of the collision history
- postproc_smash_coll.sh script that starts the postprocessing for the comparison of version 2.2.1 and J.M.'s branch
- run_smash_pf.bash script executed by launch_runs_smash_powform.sh that starts slurm jobs
- run_smash_timeless.bash script executed by launch_runs_smash_timeless.sh that starts slurm jobs
- run_smash_fragment.bash script executed by launch_runs_smash_fragment.sh that starts slurm jobs
- run_smash_coll.bash script executed by launch_runs_smash_coll.sh bash that starts slurm jobs to compare version 2.2.1 and J.M.'s branch
