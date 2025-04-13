#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=6G
#SBATCH --gpus=2
#SBATCH --gres=gpumem:20g
#SBATCH --mail-type=FAIL   

bash ./scripts/run_cuda.sh "$@"