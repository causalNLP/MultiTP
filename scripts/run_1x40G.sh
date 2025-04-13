#!/bin/bash

#SBATCH -n 1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=16G
#SBATCH --gpus=a100-pcie-40gb:1
#SBATCH --mail-type=FAIL   

bash ./scripts/run_cuda.sh "$@"