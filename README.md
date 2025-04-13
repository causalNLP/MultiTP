# MultiTP: Multilingual Trolley Problems
This repository accompanies our research paper titled "**Language Model Alignment in Multilingual Trolley Problems**" 

#### Our paper:

"**[Language Model Alignment in Multilingual Trolley Problems](https://arxiv.org/abs/2407.02273)**" by *Zhijing Jin\*, Max Kleiman-Weiner\*, Giorgio Piatti\*, Sydney Levine, Jiarui Liu, Fernando Gonzalez, Francesco Ortu, András Strausz, Mrinmaya Sachan, Rada Mihalcea, Yejin Choi, Bernhard Schölkopf*.

**Citation:**

```bibTeX
@misc{jin2024languagemodelalignmentmultilingual,
      title={Language Model Alignment in Multilingual Trolley Problems}, 
      author={Zhijing Jin and Max Kleiman-Weiner and Giorgio Piatti and Sydney Levine and Jiarui Liu and Fernando Gonzalez and Francesco Ortu and András Strausz and Mrinmaya Sachan and Rada Mihalcea and Yejin Choi and Bernhard Schölkopf},
      year={2024},
      eprint={2407.02273},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2407.02273}, 
}
```


## How to run
We various steps in the pipeline, to reproduce the results we need to run all N steps, using `multi_tp.main`.
- dataset_preparation: prepare the vignette and translate them in the target language
- query_model: query the LLM in the target language
- backtranslate: translate the LLM respose from the target language to English
- parse_choice: parse the response (left/right)

The analysis of the results can be made via `analysis/anaylsis_rq.ipynb`. Unzip the data folder to get our experimental results.

## Details
For inference we use the `pathfinder` library. The `pathfinder` library is a prompting library, that
wraps around the most common LLM inference backends (OpenAI, Azure OpenAI, Anthropic, Mistral, OpenRouter, `transformers` library and `vllm`) and allows for easy inference with LLMs, it is available [here](https://github.com/giorgiopiatti/pathfinder). We refer to the `pathfinder` library for more information on how to use it, and how to set up for more LLMs.



### Environments setup
Due to some incompatibility between the various libraries, we have 3 envs.

```bash
conda env create -f TrolleyClean.yml
conda env create -f TrolleyCleanAPI.yml
conda env create -f TrolleyCleanVLLM.yml
```



### How to run the experiments
We chained the experiments via SLURM, sometimes they may fail. assuming the setup the various env as above.


### Language experiments
    
```bash
    submit_jobs() {
    local MODEL=$1
    local SLURM_SCRIPT=$2

    local jobid=$(sbatch $SLURM_SCRIPT "TrolleyCleanVLLM" -m multi_tp.main_opt_lang steps='[query_model]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
    backtranslate_jobids=()
    # Submit backtranslate jobs for all languages in parallel
    for LANG in "${ALL_LANGUAGES[@]}"; do
        backtranslate_jobid=$(sbatch --dependency=afterok:"$jobid" ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobids+=("$backtranslate_jobid")
    done
    dependency_list=$(IFS=:; echo "afterok:${backtranslate_jobids[*]}")
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

}

submit_jobs_API() {
    local MODEL=$1
    local SLURM_SCRIPT=$2

    backtranslate_jobids=()
    # Submit backtranslate jobs for all languages in parallel
    for LANG in "${ALL_LANGUAGES[@]}"; do
        jobid=$(sbatch $SLURM_SCRIPT "TrolleyCleanAPI" -m multi_tp.main steps='[query_model]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobid=$(sbatch --dependency=afterok:"$jobid" ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobids+=("$backtranslate_jobid")
    done
    dependency_list=$(IFS=:; echo "afterok:${backtranslate_jobids[*]}")
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

    sbatch ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}

```
