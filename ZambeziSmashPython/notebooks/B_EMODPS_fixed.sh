#!/bin/sh
#SBATCH --job-name="B_EMODPS_fixed"
#SBATCH --partition=compute
#SBATCH --time=120:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem-per-cpu=1G
#SBATCH --account=research-TPM-MAS

module load 2024r1
module load openmpi/4.1.6
module load python/3.10.12
module load py-matplotlib/3.7.1
module load py-pip/23.1.2


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun python3 B_opt.py 