#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --gres=gpu:a100:2
#SBATCH --mail-type=FAIL   


# Activate the conda environment
bash ./scripts/MPG/run_cuda.sh "$@"