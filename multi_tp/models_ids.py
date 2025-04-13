MISTRAL_7B = "mistralai/Mistral-7B-Instruct-v0.2"

LLAMA_3_1_8B = "meta-llama/Meta-Llama-3.1-8B-Instruct"
LLAMA_3_1_70B = "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8"

LLAMA_3_8B = "meta-llama/Meta-Llama-3-8B-Instruct"
LLAMA_3_70B = "neuralmagic/Meta-Llama-3-70B-Instruct-FP8"


LLAMA_2_70B = "meta-llama/Llama-2-70b-chat-hf"
LLAMA_2_13B = "meta-llama/Llama-2-13b-chat-hf"
LLAMA_2_7B = "meta-llama/Llama-2-7b-chat-hf"

QWEN_2_7B = "Qwen/Qwen2-7B-Instruct"
QWEN_2_72B = "Qwen/Qwen2-72B-Instruct-GPTQ-Int8"

PHI_3_MEDIUM = "microsoft/Phi-3-medium-4k-instruct"
PHI_3_5_MINI = "microsoft/Phi-3.5-mini-instruct"
PHI_3_5_MOE = "microsoft/Phi-3.5-MoE-instruct"

GEMMA_2_9B = "google/gemma-2-9b-it"
GEMMA_2_2B = "google/gemma-2b-it"
GEMMA_2_27B = "google/gemma-2-27b-it"
GPT_4_OMNI_MINI = "gpt-4o-mini-2024-07-18"

GPT_4 = "gpt-4-0613"
GPT_3 = "text-davinci-003"

MODELS = [
    MISTRAL_7B,
    LLAMA_3_1_8B,
    LLAMA_3_1_70B,
    LLAMA_3_8B,
    LLAMA_3_70B,
    LLAMA_2_70B,
    LLAMA_2_13B,
    LLAMA_2_7B,
    QWEN_2_7B,
    QWEN_2_72B,
    PHI_3_MEDIUM,
    PHI_3_5_MINI,
    PHI_3_5_MOE,
    GEMMA_2_9B,
    GEMMA_2_2B,
    GEMMA_2_27B,
    GPT_4_OMNI_MINI,
    GPT_4,
    GPT_3,
]


# LLM models information dictionary
llm_models = {
    MISTRAL_7B: {
        "release_date": "2023-12",
        "pretty_name": "Mistral 7B",
        "family": "Mistral",
        "size": "7B",
        "version": "2",
    },
    LLAMA_3_1_8B: {
        "release_date": "2024-07",
        "pretty_name": "Llama 3.1 8B",
        "family": "Llama",
        "size": "8B",
        "version": "3.1",
    },
    LLAMA_3_1_70B: {
        "release_date": "2024-07",
        "pretty_name": "Llama 3.1 70B",
        "family": "Llama",
        "size": "70B",
        "version": "3.1",
    },
    LLAMA_3_8B: {
        "release_date": "2024-04",
        "pretty_name": "Llama 3 8B",
        "family": "Llama",
        "size": "8B",
        "version": "3",
    },
    LLAMA_3_70B: {
        "release_date": "2024-04",
        "pretty_name": "Llama 3 70B",
        "family": "Llama",
        "size": "70B",
        "version": "3",
    },
    LLAMA_2_70B: {
        "release_date": "2023-07",
        "pretty_name": "Llama 2 70B",
        "family": "Llama",
        "size": "70B",
        "version": "2",
    },
    LLAMA_2_13B: {
        "release_date": "2023-07",
        "pretty_name": "Llama 2 13B",
        "family": "Llama",
        "size": "13B",
        "version": "2",
    },
    LLAMA_2_7B: {
        "release_date": "2023-07",
        "pretty_name": "Llama 2 7B",
        "family": "Llama",
        "size": "7B",
        "version": "2",
    },
    QWEN_2_72B: {
        "release_date": "2024-06",
        "pretty_name": "Qwen 2 72B",
        "family": "Qwen",
        "size": "72B",
        "version": "2",
    },
    QWEN_2_7B: {
        "release_date": "2024-06",
        "pretty_name": "Qwen 2 7B",
        "family": "Qwen",
        "size": "7B",
        "version": "2",
    },
    PHI_3_MEDIUM: {
        "release_date": "2024-05",
        "pretty_name": "Phi-3 Medium",
        "family": "Phi",
        "size": "14B",
        "version": "3",
    },
    PHI_3_5_MINI: {
        "release_date": "2024-08",
        "pretty_name": "Phi-3.5 Mini",
        "family": "Phi",
        "size": "4B",
        "version": "3.5",
    },
    PHI_3_5_MOE: {
        "release_date": "2024-08",
        "pretty_name": "Phi-3.5 MoE",
        "family": "Phi",
        "size": "42B",
        "version": "3.5",
    },
    GEMMA_2_9B: {
        "release_date": "2024-06",
        "pretty_name": "Gemma 2 9B",
        "family": "Gemma",
        "size": "9B",
        "version": "2",
    },
    GEMMA_2_2B: {
        "release_date": "2024-07",
        "pretty_name": "Gemma 2 2B",
        "family": "Gemma",
        "size": "2B",
        "version": "2",
    },
    GEMMA_2_27B: {
        "release_date": "2024-06",
        "pretty_name": "Gemma 2 27B",
        "family": "Gemma",
        "size": "27B",
        "version": "2",
    },
    GPT_4_OMNI_MINI: {
        "release_date": "2024-07",
        "pretty_name": "GPT-4o Mini",
        "family": "GPT",
        "size": "Mini",
        "version": "4",
    },
    GPT_4: {
        "release_date": "2024-06",
        "pretty_name": "GPT-4",
        "family": "GPT",
        "size": "4",
        "version": "4",
    },
    GPT_3: {
        "release_date": "2022-11",
        "pretty_name": "GPT-3",
        "family": "GPT",
        "size": "3",
        "version": "3",
    },
}


def get_model_release_date(model):
    return llm_models[model]["release_date"]


def get_family(model):
    return llm_models[model]["family"]


def get_size(model):
    return llm_models[model]["size"]


def get_version(model):
    return llm_models[model]["version"]


def get_pretty_name(model):
    return llm_models[model]["pretty_name"]
