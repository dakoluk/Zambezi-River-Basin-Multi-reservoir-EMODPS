#!/bin/sh
#SBATCH --job-name="B_EMODPS"
#SBATCH --partition=compute
#SBATCH --time=120:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem-per-cpu=1G
#SBATCH --account=research-TPM-MAS


module load 2023r1
module load python/3.8.12

module load py-numpy/1.22.4
module load py-scipy
module load py-matplotlib
module load py-pip/21.1.2


pip install pandas
pip install ema-workbench
pip install openpyxl

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun python3 B_opt.py 