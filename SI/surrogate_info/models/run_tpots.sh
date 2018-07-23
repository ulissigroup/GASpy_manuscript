#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=08:00:00
#SBATCH --job-name=tpots
#SBATCH --output=tpots-%j.out
#SBATCH --error=tpots-%j.error
#SBATCH --constraint=haswell
#SBATCH --qos=premium

python run_tpots.py
