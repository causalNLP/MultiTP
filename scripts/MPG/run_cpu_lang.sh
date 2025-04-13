#!/bin/bash
#SBATCH --array=0-106%30

# Define the array of languages
ALL_LANGUAGES=(
  af am ar az be bg bn bs ca ceb co cs cy da de el en eo es et eu fa "fi" fr fy
  ga gd gl gu ha haw he hi hmn hr ht hu hy id ig is it iw ja jw ka kk km kn
  ko ku ky la lb lo lt lv mg mi mk ml mn mr ms mt my ne nl no ny or pa pl ps
  pt ro ru sd si sk sl sm sn so sq sr st su sv sw ta te tg th tl tr ug uk ur
  uz vi xh yi yo zh-cn zh-tw zu
)

# Get the language for this task based on the array task ID
LANG=${ALL_LANGUAGES[$SLURM_ARRAY_TASK_ID]}

# Set your variables
MODEL=$1
LLAMA_3_1_8B="meta-llama/Meta-Llama-3.1-8B-Instruct" 

# Run the backtranslate step
srun ./scripts/MPG/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

# Wait for all tasks to complete
wait