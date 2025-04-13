import hydra
from hydra import compose, initialize
from hydra.core.global_hydra import GlobalHydra
from omegaconf import DictConfig, OmegaConf

from .step_back_translate import BackTranslation
from .step_parse_choice import ParseChoice
from .step_performance_summary import PerformanceSummary
from .step_prepare_dataset import DatasetGenerator
from .step_query_model import QueryModel
from .system_prompts import SystemPromptGenerator
from .utils import LANGUAGES


@hydra.main(version_base=None, config_path="conf", config_name="default")
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))
    lang = LANGUAGES
    if cfg.lang_subset == "consistency":
        lang = [
            "ar",
            "bn",
            "zh-cn",
            "en",
            "fr",
            "de",
            "hi",
            "ja",
            "km",
            "sw",
            "ur",
            "yo",
            "zu",
            "my",
            "ug",
        ]

    for lang in lang:
        try:
            if "dataset_preparation" in cfg.steps:
                dataset_generator = DatasetGenerator(
                    lang=lang,
                    country=cfg.country,
                    add_paraphrase=cfg.add_paraphrase,
                    translator_provider_forward=cfg.translation_forward_model,
                )
                dataset_generator.prepare_dataset()

                system_prompt_generator = SystemPromptGenerator(
                    lang=lang,
                    system_role=cfg.system_role,
                    translator_provider_forward=cfg.translation_forward_model,
                )
                system_prompt_generator.translate_system_prompt()
            if "query_model" in cfg.steps:
                query_model = QueryModel(
                    model_version=cfg.model_version,
                    system_role=cfg.system_role,
                    lang=lang,
                    country=cfg.country,
                    add_paraphrase=cfg.add_paraphrase,
                    translator_provider_forward=cfg.translation_forward_model,
                )
                query_model.run()

            if "backtranslate" in cfg.steps:
                back_translation = BackTranslation(
                    model_version=cfg.model_version,
                    system_role=cfg.system_role,
                    lang=lang,
                    country=cfg.country,
                    add_paraphrase=cfg.add_paraphrase,
                    translator_provider_forward=cfg.translation_forward_model,
                    translator_provider_backward=cfg.translation_backward_model,
                )
                back_translation.run()

            if "parse_choice" in cfg.steps:
                choice_parser = ParseChoice(
                    model_version=cfg.model_version,
                    system_role=cfg.system_role,
                    lang=lang,
                    country=cfg.country,
                    add_paraphrase=cfg.add_paraphrase,
                    translator_provider_forward=cfg.translation_forward_model,
                    translator_provider_backward=cfg.translation_backward_model,
                    analysis_backend_model_version=cfg.analysis_backend_model_version,
                )
                choice_parser.run()

            if "performance_summary" in cfg.steps:
                performance = PerformanceSummary(
                    model_version=cfg.model_version,
                    system_role=cfg.system_role,
                    lang=lang,
                    country=cfg.country,
                    add_paraphrase=cfg.add_paraphrase,
                    translator_provider_forward=cfg.translation_forward_model,
                    translator_provider_backward=cfg.translation_backward_model,
                    analysis_backend_model_version=cfg.analysis_backend_model_version,
                )
                performance.run()
        except Exception as e:
            print(f"Error for language {lang}: {e}")


if __name__ == "__main__":
    main()
