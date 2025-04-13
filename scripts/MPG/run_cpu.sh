#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=64G
#SBATCH --mail-type=FAIL  

bash ./scripts/MPG/run_cuda.sh "$@"