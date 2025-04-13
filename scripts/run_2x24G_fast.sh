#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=6G
#SBATCH --gpus=rtx_3090:2
#SBATCH --mail-type=FAIL   

bash ./scripts/run_cuda.sh "$@"