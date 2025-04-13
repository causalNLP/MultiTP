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


@hydra.main(version_base=None, config_path="conf", config_name="default")
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))

    if "dataset_preparation" in cfg.steps:
        dataset_generator = DatasetGenerator(
            lang=cfg.lang,
            country=cfg.country,
            add_paraphrase=cfg.add_paraphrase,
            translator_provider_forward=cfg.translation_forward_model,
        )
        dataset_generator.prepare_dataset()

        system_prompt_generator = SystemPromptGenerator(
            lang=cfg.lang,
            system_role=cfg.system_role,
            translator_provider_forward=cfg.translation_forward_model,
        )
        system_prompt_generator.translate_system_prompt()
    if "query_model" in cfg.steps:
        query_model = QueryModel(
            model_version=cfg.model_version,
            system_role=cfg.system_role,
            lang=cfg.lang,
            country=cfg.country,
            add_paraphrase=cfg.add_paraphrase,
            translator_provider_forward=cfg.translation_forward_model,
        )
        query_model.run()

    if "backtranslate" in cfg.steps:
        back_translation = BackTranslation(
            model_version=cfg.model_version,
            system_role=cfg.system_role,
            lang=cfg.lang,
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
            lang=cfg.lang,
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
            lang=cfg.lang,
            country=cfg.country,
            add_paraphrase=cfg.add_paraphrase,
            translator_provider_forward=cfg.translation_forward_model,
            translator_provider_backward=cfg.translation_backward_model,
            analysis_backend_model_version=cfg.analysis_backend_model_version,
        )
        performance.run()


if __name__ == "__main__":
    main()
