import os

import pandas as pd
from efficiency.log import fread
from tqdm import tqdm

from multi_tp.translation import get_translator
from multi_tp.utils import (
    LANGUAGES,
    dataset_back_translated_file_tmpl,
    dataset_file_tmpl,
)


class BackTranslationDataset:
    def __init__(self, lang, translator_provider_forward):
        self.lang = lang
        self.translator_provider_forward = translator_provider_forward

    def run(self):
        translator = get_translator(self.translator_provider_forward)
        dataset_path = dataset_file_tmpl.format(
            lang=self.lang,
            translator_provider_forward=self.translator_provider_forward,
            suffix="",
        )

        out_path = dataset_back_translated_file_tmpl.format(
            lang=self.lang,
            translator_provider_forward=self.translator_provider_forward,
            suffix="",
        )
        if os.path.exists(out_path):
            print(f"File exists: {out_path}")
            return

        dataset = fread(dataset_path)
        for row in tqdm(dataset, desc=self.lang):
            res = translator.back_translate(self.lang, row["Prompt"])
            row["prompt_en_back_translated"] = res

        df = pd.DataFrame(dataset)
        df.to_csv(
            out_path,
            index=False,
        )


import hydra
from hydra import compose, initialize
from hydra.core.global_hydra import GlobalHydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="conf", config_name="default")
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))

    s = BackTranslationDataset(
        lang=cfg.lang, translator_provider_forward=cfg.translation_forward_model
    )
    s.run()


if __name__ == "__main__":
    main()
