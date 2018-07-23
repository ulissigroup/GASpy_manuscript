#!/bin/sh

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=06:00:00
#SBATCH --partition=regular
#SBATCH --job-name=rut_tpot
#SBATCH --output=run_tpot-%j.out
#SBATCH --error=run_tpot-%j.error
#SBATCH --constraint=haswell
#SBATCH --qos=premium


python long_tpot.py
