#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=2G
#SBATCH --mail-type=FAIL   

bash ./scripts/run_cuda.sh "$@"