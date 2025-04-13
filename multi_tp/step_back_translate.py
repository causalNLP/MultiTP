import os

import pandas as pd
from efficiency.log import fread, write_dict_to_csv
from tqdm import tqdm

from .translation import get_translator
from .utils import (
    cache_back_responses_tmpl,
    cache_responses_tmpl,
    get_model_name_path,
    get_suffix,
)


class BackTranslation:

    def __init__(
        self,
        model_version,
        system_role,
        lang,
        country,
        add_paraphrase,
        translator_provider_forward,
        translator_provider_backward,
    ):
        self.lang = lang
        self.in_path = cache_responses_tmpl.format(
            model_version=get_model_name_path(model_version),
            system_role=system_role,
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
        )
        self.out_path = cache_back_responses_tmpl.format(
            model_version=get_model_name_path(model_version),
            system_role=system_role,
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
            translator_provider_backward=translator_provider_backward,
        )

        os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

        self.translator_provider_backward = translator_provider_backward
        if lang == "en":
            self.translator = None
        else:
            self.translator = get_translator(translator_provider_backward)

    def run(self):
        dataset = fread(self.in_path)
        if len(dataset) == 0:
            print(f"Skipping {self.in_path} No data")
            return

        responses = []
        print(f"Back translation form {self.lang} to English")

        # Check if output file already exists and has data, then skip
        if os.path.exists(self.out_path):
            if len(fread(self.out_path)) > 0:
                print(f"Skipping {self.out_path}")
                return

        for row in tqdm(dataset, desc=self.out_path):
            if self.translator is None:
                row["gpt_response_en"] = row["gpt_response_raw"]
            else:
                row["gpt_response_en"] = self.translator.back_translate(
                    self.lang, row["gpt_response_raw"]
                )
            row["translator_provider_backward"] = self.translator_provider_backward
            responses.append(row)

        df = pd.DataFrame(responses)
        df.to_csv(self.out_path, index=False)
