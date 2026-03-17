#!/bin/sh
#
#SBATCH --job-name="prospective-inverse-modelling"
#SBATCH --partition=compute-p1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=3000M
#SBATCH --output=output_%j.log         # Output file name (%j expands to jobID)
#SBATCH --error=error_%j.log           # Error file name (%j expands to jobID)
#SBATCH --time=02:00:00
#SBATCH --ntasks-per-node=1
#SBATCH --account=research-TPM-ESS
#SBATCH --mail-type=ALL                # Mail events (NONE, BEGIN, END, FAIL, ALL)
module purge
module load slurm
module load .compiler-2024
module load 2024r1
module load openjdk/17.0.8.1_1 # this gives java, javac, and jar
module load python/3.10.12

source venv310/bin/activate
cd prospective-inverse-sampling/

python3.10 main.py
