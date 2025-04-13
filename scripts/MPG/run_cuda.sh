set -e # fail fully on first line failure

# Check that the correct number of arguments is provided
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <conda_env> <command> [args...]"
  exit 1
fi

# Extract the conda environment from the first argument
CONDA_ENV="$1"
shift

# Activate the conda environment
source ~/.bashrc
# module load  stack/2024-05 gcc/13.2.0 eth_proxy # python_cuda/3.11.6 cuda/12.1.1
conda activate "$CONDA_ENV"

# Store the job command
JOB_CMD=("$@")
HYDRA_FULL_ERROR=1
# Print and run the job command
echo "Running command: python3 ${JOB_CMD[@]}"
python3 "${JOB_CMD[@]}"