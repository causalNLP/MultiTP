#!/bin/zsh

### API models
GPT_4_0613="z-gpt-4-0613"
GPT_4="z-gpt-4-turbo-2024-04-09" # "gpt-4-0125-preview"
GPT_3_5="gpt-3.5-turbo-0125"

GPT_4_OMNI="z-gpt-4o-2024-08-06"
GPT_4_OMNI_MINI="gpt-4o-mini-2024-07-18"

MISTRAL_LARGE="mistral-large-2402"
MISTRAL_MEDIUM="mistral-medium-2312"

CLAUDE_3_OPUS="claude-3-opus-20240229"
CLAUDE_3_SONNET="claude-3-sonnet-20240229"
CLAUDE_3_HAIKU="claude-3-haiku-20240307"

### Local models
MISTRAL_7B="mistralai/Mistral-7B-Instruct-v0.2" # 2x24G


LLAMA_3_8B="meta-llama/Meta-Llama-3-8B-Instruct" 
LLAMA_3_70B="neuralmagic/Meta-Llama-3-70B-Instruct-FP8" 

LLAMA_3_1_8B="meta-llama/Meta-Llama-3.1-8B-Instruct" 
LLAMA_3_1_70B="neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" 
LLAMA_3_1_405B_QUANT="hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4"

LLAMA_2_70B="meta-llama/Llama-2-70b-chat-hf"
LLAMA_2_13B="meta-llama/Llama-2-13b-chat-hf" # 3x24G
LLAMA_2_7B="meta-llama/Llama-2-7b-chat-hf" # 2x24G

QWEN_1_5_7B="Qwen/Qwen1.5-7B-Chat"

QWEN_2_7B="Qwen/Qwen2-7B-Instruct"
QWEN_2_72B="Qwen/Qwen2-72B-Instruct-GPTQ-Int8"

GEMMA_2_9B="google/gemma-2-9b-it"
GEMMA_2_2B="google/gemma-2b-it"
GEMMA_2_27B="google/gemma-2-27b-it"

PHI_3_MEDIUM="microsoft/Phi-3-medium-4k-instruct"
PHI_3_5_MINI="microsoft/Phi-3.5-mini-instruct"
PHI_3_5_MOE="microsoft/Phi-3.5-MoE-instruct"

ALL_LANGUAGES=(
  af am ar az be bg bn bs ca ceb co cs cy da de el en eo es et eu fa "fi" fr fy
  ga gd gl gu ha haw he hi hmn hr ht hu hy id ig is it iw ja jw ka kk km kn
  ko ku ky la lb lo lt lv mg mi mk ml mn mr ms mt my ne nl no ny or pa pl ps
  pt ro ru sd si sk sl sm sn so sq sr st su sv sw ta te tg th tl tr ug uk ur
  uz vi xh yi yo zh-cn zh-tw zu
)


ALL_COUNTRIES=('abw'
 'afg'
 'ago'
 'aia'
 'ala'
 'alb'
 'and'
 'are'
 'arg'
 'arm'
 'asm'
 'ata'
 'atf'
 'atg'
 'aus'
 'aut'
 'aze'
 'bdi'
 'bel'
 'ben'
 'bes'
 'bfa'
 'bgd'
 'bgr'
 'bhr'
 'bhs'
 'bih'
 'blm'
 'blr'
 'blz'
 'bmu'
 'bol'
 'bra'
 'brb'
 'brn'
 'btn'
 'bvt'
 'bwa'
 'caf'
 'can'
 'cck'
 'che'
 'chl'
 'chn'
 'civ'
 'cmr'
 'cod'
 'cog'
 'cok'
 'col'
 'com'
 'cpv'
 'cri'
 'cub'
 'cuw'
 'cxr'
 'cym'
 'cyp'
 'cze'
 'deu'
 'dji'
 'dma'
 'dnk'
 'dom'
 'dza'
 'ecu'
 'egy'
 'eri'
 'esh'
 'esp'
 'est'
 'eth'
 'fin'
 'fji'
 'flk'
 'fra'
 'fro'
 'fsm'
 'gab'
 'gbr'
 'geo'
 'ggy'
 'gha'
 'gib'
 'gin'
 'glp'
 'gmb'
 'gnb'
 'gnq'
 'hmd'
 'hnd'
 'hrv'
 'hti'
 'hun'
 'idn'
 'imn'
 'ind'
 'iot'
 'irl'
 'irn'
 'irq'
 'isl'
 'isr'
 'ita'
 'jam'
 'jey'
 'jor'
 'jpn'
 'kaz'
 'ken'
 'kgz'
 'khm'
 'kir'
 'kna'
 'kor'
 'kwt'
 'lao'
 'lbn'
 'lbr'
 'lby'
 'lca'
 'lie'
 'lka'
 'lso'
 'ltu'
 'lux'
 'lva'
 'mac'
 'maf'
 'mar'
 'mco'
 'mda'
 'mdg'
 'mdv'
 'mex'
 'mhl'
 'mkd'
 'mli'
 'mlt'
 'mmr'
 'mne'
 'mng'
 'mnp'
 'moz'
 'mrt'
 'msr'
 'mtq'
 'mus'
 'mwi'
 'mys'
 'myt'
 'nam'
 'ncl'
 'ner'
 'nfk'
 'nga'
 'nic'
 'niu'
 'nld'
 'nor'
 'npl'
 'nru'
 'nzl'
 'omn'
 'pak'
 'pan'
 'pcn'
 'per'
 'phl'
 'plw'
 'png'
 'pol'
 'pri'
 'prk'
 'prt'
 'pry'
 'pse'
 'pyf'
 'qat'
 'reu'
 'rou'
 'rus'
 'rwa'
 'sau'
 'sdn'
 'sen'
 'sgp'
 'sgs'
 'shn'
 'sjm'
 'slb'
 'sle'
 'slv'
 'smr'
 'som'
 'spm'
 'srb'
 'ssd'
 'stp'
 'sur'
 'svk'
 'svn'
 'swe'
 'swz'
 'sxm'
 'syc'
 'syr'
 'tca'
 'tcd'
 'tgo'
 'tha'
 'tjk'
 'tkl'
 'tkm'
 'tls'
 'ton'
 'tto'
 'tun'
 'tur'
 'tuv'
 'twn'
 'tza'
 'uga'
 'ukr'
 'umi'
 'ury'
 'usa'
 'uzb'
 'vat'
 'vct'
 'ven'
 'vgb'
 'vir'
 'vnm'
 'vut'
 'wlf'
 'wsm'
 'yem'
 'zaf'
 'zmb'
 'zwe' )


# ONLY once to prepare the dataset


LANGUAGES_CONSISTENCY=(ar bn zh-cn en fr de hi ja km sw ur yo zu my ug)
for LANG in "${LANGUAGES_CONSISTENCY[@]}"; do
    jobid_dataset=$(sbatch ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps=['dataset_preparation'] lang=$LANG add_paraphrase=True | awk '{print $4}')
done

# for COUNTRY in "${ALL_COUNTRIES[@]}"; do
#     jobid_dataset=$(sbatch ./scripts/run_cpu_small.sh "TrolleyClean" -m multi_tp.main steps=['dataset_preparation'] country=$COUNTRY lang='en' | awk '{print $4}')
# done

# Submit job chain for each language
# MODEL=$LLAMA_3_1_8B
# SLURM_SCRIPT="./scripts/run_2x24G_fast.sh"

# for LANG in "${LANGUAGES[@]}"; do
#     # jobid_dataset=$(sbatch ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[dataset_preparation]' lang=$LANG | awk '{print $4}')
#     # jobid=$(sbatch --dependency=afterok:$jobid_dataset $SLURM_SCRIPT "TrolleyClean" -m multi_tp.main steps='[query_model]' lang=$LANG model_version=$MODEL | awk '{print $4}')
#     # jobid=$(sbatch $SLURM_SCRIPT "TrolleyCleanVLLM" -m multi_tp.main steps='[query_model]' lang=$LANG model_version=$MODEL | awk '{print $4}')
#     jobid=$(sbatch ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL | awk '{print $4}')
#     jobid=$(sbatch --dependency=afterok:$jobid ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM" -m multi_tp.main steps='[parse_choice, performance_summary]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
# done

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
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

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
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

    sbatch ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}



# submit_jobs_API $GPT_4_OMNI_MINI "./scripts/run_cpu.sh"

resume_from_backtrans_submit_jobs() {
    local MODEL=$1

    backtranslate_jobids=()
    # Submit backtranslate jobs for all languages in parallel
    for LANG in "${ALL_LANGUAGES[@]}"; do
        backtranslate_jobid=$(sbatch ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobids+=($backtranslate_jobid)
    done

    # jobid=$(sbatch ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
    dependency_list=$(IFS=:; echo "afterok:${backtranslate_jobids[*]}")
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}

# resume_from_backtrans_submit_jobs() {
#     local MODEL=$1

#     sbatch ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
# }



# resume_from_backtrans_submit_jobs $QWEN_2_72B 
# resume_from_backtrans_submit_jobs $LLAMA_2_70B #issues




# resume_from_backtrans_submit_jobs $LLAMA_3_1_70B 
# resume_from_backtrans_submit_jobs $LLAMA_3_8B 


# resume_from_backtrans_submit_jobs $PHI_3_5_MINI   #issues
# resume_from_backtrans_submit_jobs $PHI_3_5_MOE #issues

# resume_from_backtrans_submit_jobs $GEMMA_2_9B 
# resume_from_backtrans_submit_jobs $GEMMA_2_2B
# resume_from_backtrans_submit_jobs $GEMMA_2_2







# resume_from_backtrans_submit_jobs $GEMMA_2_27B "./scripts/run_4x24G_fast.sh" From backtranslation
# submit_jobs $PHI_3_5_MINI "./scripts/run_2x24G_fast.sh" # From query 
# resume_from_backtrans_submit_jobs $PHI_3_5_MOE "./scripts/run_1x80G.sh" # ALL

# ALLDONER
# resume_from_backtrans_submit_jobs $LLAMA_2_13B "./scripts/run_1x40G.sh" # DONE
# submit_jobs $LLAMA_2_7B "./scripts/run_2x24G_fast.sh" # DONE
# submit_jobs $LLAMA_3_1_70B "./scripts/run_4x80G.sh"  #th

# submit_jobs $MISTRAL_7B "./scripts/run_2x24G_fast.sh" #DONE
# submit_jobs $QWEN_2_7B "./scripts/run_2x24G_fast.sh" #DONE
# submit_jobs $PHI_3_MEDIUM "./scripts/run_2x24G_fast.sh" #DONE



  
# USE THIS IF NEED TO RESUME FORM BACKTRANSLATION
resume_from_backtrans_submit_jobs_SUBSET() {
    local MODEL=$1
    local SLURM_SCRIPT=$2
    # all remaining args
    local LANGUAGES=("${@:3}")

    backtranslate_jobids=()
    # Submit backtranslate jobs for all languages in parallel
    for LANG in "${LANGUAGES[@]}"; do
        backtranslate_jobid=$(sbatch ./scripts/run_cpu.sh "TrolleyClean" -m multi_tp.main steps='[backtranslate]' lang=$LANG model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobids+=($backtranslate_jobid)
    done
    dependency_list=$(IFS=:; echo "afterok:${backtranslate_jobids[*]}")
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_lang steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}

# MISSING=(he iw yi yo)
# resume_from_backtrans_submit_jobs $QWEN_2_72B "${MISSING[@]}"
# MISSING=(lo su)
# resume_from_backtrans_submit_jobs $LLAMA_2_70B "${MISSING[@]}"


# MISSING=(ja)
# resume_from_backtrans_submit_jobs $LLAMA_3_1_70B "${MISSING[@]}"

# MISSING=(gl hr ig my tr)
# resume_from_backtrans_submit_jobs $LLAMA_3_8B "${MISSING[@]}"

# MISSING=(eo et eu hy is ky sl sm st ug xh zu)
# resume_from_backtrans_submit_jobs $PHI_3_5_MINI "${MISSING[@]}"
# MISSING=(ar bn haw ml my)
# resume_from_backtrans_submit_jobs $PHI_3_5_MOE "${MISSING[@]}"

# MISSING=(be bn ca fa "fi" fr fy hu jw ka kk km ku la mk mr no pa pl sn sr sv ta th ur)
# resume_from_backtrans_submit_jobs $GEMMA_2_9B "${MISSING[@]}"
# MISSING=(ka kk)
# resume_from_backtrans_submit_jobs $GEMMA_2_2B "${MISSING[@]}"
# MISSING=(af bs de fr hr jw ky ml no pa ro sd si tr)
# resume_from_backtrans_submit_jobs $GEMMA_2_27B "${MISSING[@]}"
# MISSING=(yi)
# resume_from_backtrans_submit_jobs $GPT_4_OMNI_MINI "${MISSING[@]}"




# MISSING=(th uk)
# resume_from_backtrans_submit_jobs_SUBSET $LLAMA_3_1_8B "./scripts/run_2x24G_fast.sh" "${MISSING[@]}"
# MISSING=(th)
# resume_from_backtrans_submit_jobs_SUBSET $LLAMA_3_1_70B "./scripts/run_2x24G_fast.sh" "${MISSING[@]}"
# MISSING=(gl hr ig my tr)
# resume_from_backtrans_submit_jobs_SUBSET $LLAMA_3_8B "./scripts/run_2x24G_fast.sh" "${MISSING[@]}"
# # MISSING=(be bn ca fa "fi" fr fy hu jw ka kk km ku la mk mr no pa pl sn sr sv ta th ur) 
# # resume_from_backtrans_submit_jobs_SUBSET $GEMMA_2_9B "./scripts/run_2x24G_fast.sh" "${MISSING[@]}"
# # MISSING=(ka kk ml mr sv vi yo zh-cn zh-tw zu)
# # resume_from_backtrans_submit_jobs_SUBSET $GEMMA_2_2B "./scripts/run_1x24G_fast.sh" "$MISSING"


# sbatch ./scripts_country/run_2x24G_fast.sh TrolleyCleanVLLM '[parse_choice, performance_summary]' microsoft/Phi-3-medium-4k-instruct
# sbatch ./scripts/run_2x24G_fast.sh TrolleyCleanVLLM '[parse_choice, performance_summary]' meta-llama/Meta-Llama-3.1-8B-Instruct


# Note only english
submit_jobs_country() {
    local MODEL=$1
    local SLURM_SCRIPT=$2
    local jobid=$(sbatch $SLURM_SCRIPT "TrolleyCleanVLLM" '[query_model, backtranslate]' $MODEL | awk '{print $4}')
    # is English only, so backtranslate is only a copy.
    sbatch --dependency=afterok:"$jobid" ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_country steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}



# # submit_jobs_country $MISTRAL_7B " "

# # submit_jobs_country $LLAMA_3_1_8B " "
# submit_jobs_country $LLAMA_3_1_70B " "

# # submit_jobs_country $LLAMA_3_8B  " "
# # submit_jobs_country $LLAMA_3_70B  " "

# submit_jobs_country $QWEN_2_7B " "
# submit_jobs_country $QWEN_2_72B " "

# submit_jobs_country $LLAMA_2_70B " "

# submit_jobs_country $LLAMA_2_13B " "

# # submit_jobs_country $GEMMA_2_27B " "

# submit_jobs_country $GEMMA_2_9B " "
# # submit_jobs_country $GEMMA_2_2B " "

# # submit_jobs_country $PHI_3_5_MINI " "

# submit_jobs_country $PHI_3_5_MOE " "


# # submit_jobs_country $PHI_3_MEDIUM " "




submit_jobs_country_API() {
    local MODEL=$1

    backtranslate_jobids=()
    for COUNTRY in "${ALL_COUNTRIES[@]}"; do
        jobid=$(sbatch "./scripts/run_cpu.sh" "TrolleyCleanAPI" -m multi_tp.main steps='[query_model, backtranslate]' lang=en country=$COUNTRY model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B | awk '{print $4}')
        backtranslate_jobids+=($jobid)
    done
    dependency_list=$(IFS=:; echo "afterok:${backtranslate_jobids[*]}")
    sbatch --dependency=$dependency_list ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_country steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B

    # sbatch ./scripts/run_2x24G_fast.sh "TrolleyCleanVLLM"  -m multi_tp.main_opt_country steps='[parse_choice, performance_summary]' model_version=$MODEL analysis_backend_model_version=$LLAMA_3_1_8B
}

# submit_jobs_country_API $GPT_4_OMNI_MINI 