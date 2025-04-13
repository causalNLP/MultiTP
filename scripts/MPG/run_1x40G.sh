#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --gres=gpu:a100:1
#SBATCH --mail-type=FAIL   


# Activate the conda environment
bash ./scripts/MPG/run_cuda.sh "$@"