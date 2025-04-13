import os

import transformers
from efficiency.log import fread, write_dict_to_csv
from tqdm import tqdm

from .system_prompts import SystemPromptLoader
from .utils import (
    cache_responses_tmpl,
    dataset_file_tmpl,
    get_llm_model,
    get_model_name_path,
    get_suffix,
)

# class PathFinderAdapter:

#     def __init__(self, model_version, max_tokens, system_prompt) -> None:
#         self.system_prompt = system_prompt
#         self.max_tokens = max_tokens
#         self.model = get_model(model_version)

#     def ask(self, query):
#         """
#         Should return raw_response, raw_entire_output
#         """

#         lm = self.model
#         with system():
#             lm += self.system_prompt
#         with user():
#             lm += query
#         with assistant():
#             lm += gen(name="response_text", max_tokens=self.max_tokens, temperature=0.0)

#         response_text = lm["response_text"]
#         raw_response = response_text
#         return raw_response


class QueryModel:

    def __init__(
        self,
        model_version,
        system_role,
        lang,
        country,
        add_paraphrase,
        translator_provider_forward,
    ):
        self.lang = lang
        self.system_role = system_role
        self.translator_provider_forward = translator_provider_forward
        self.model_version = model_version
        self.country = country

        self.dataset_path = dataset_file_tmpl.format(
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
        )

        self.out_path = cache_responses_tmpl.format(
            model_version=get_model_name_path(model_version),
            system_role=system_role,
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
        )
        os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

        system_prompt_loader = SystemPromptLoader(
            lang=lang,
            system_role=system_role,
            translator_provider_forward=translator_provider_forward,
        )
        self.system_prompt = system_prompt_loader.get_system_prompt()

        self.query_provider = get_llm_model(
            model_version=model_version,
            max_tokens=1024,
            system_prompt=self.system_prompt,
        )

    def run(self):
        dataset = fread(self.dataset_path)
        if len(dataset) == 0:
            print(f"Skipping {self.dataset_path} No data")
            return
        # Check if output file already exists and has data, then skip
        if os.path.exists(self.out_path):
            if len(fread(self.out_path)) > 0:
                print(f"Skipping {self.out_path}")
                return
        responses = []
        dataset_prompts = [row["Prompt"] for row in dataset]
        dataset_res = self.query_provider.ask_batch(dataset_prompts)
        for row, res in tqdm(zip(dataset, dataset_res), desc=self.out_path):
            row["gpt_response_raw"] = res
            # Log parameters
            row["lang"] = self.lang
            row["system_role"] = self.system_role
            row["translator_provider_forward"] = self.translator_provider_forward
            row["model"] = self.model_version
            row["country"] = self.country
            responses.append(row)

        import pandas as pd

        df = pd.DataFrame(responses)
        df.to_csv(self.out_path, index=False)
