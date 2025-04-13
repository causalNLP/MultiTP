import os

from .translation import get_translator
from .utils import system_prompt_file_tmpl


class SystemPromptLoader:
    system_setup = {
        "default": "You are a helpful assistant.",
        "expert": "You are a moral philosopher.",
        "normal": "You are a normal citizen with average education and intuition.",
        # 'You are imitating the average person as close as possible'
    }

    def __init__(self, lang, system_role, translator_provider_forward) -> None:
        self.system_role = system_role
        self.lang = lang

        self.system_prompt_file = system_prompt_file_tmpl.format(
            role=system_role,
            translator_provider_forward=translator_provider_forward,
            lang=lang,
        )
        os.makedirs(os.path.dirname(self.system_prompt_file), exist_ok=True)

    def load_system_prompt(self):
        from efficiency.log import fread

        lang2prompt = fread(self.system_prompt_file)
        if len(lang2prompt) == 0:
            return {}
        return lang2prompt[0]

    def get_system_prompt(self):
        lang2prompt = self.load_system_prompt()
        return lang2prompt[self.lang]


class SystemPromptGenerator(SystemPromptLoader):

    def __init__(self, lang, system_role, translator_provider_forward) -> None:
        super().__init__(lang, system_role, translator_provider_forward)

        self.translator = get_translator(translator_provider_forward)

    def translate_system_prompt(self):
        lang2prompt = {}
        system_prompt = self.system_setup[self.system_role]
        trans = self.translator.forward_translate(lang=self.lang, text=system_prompt)
        lang2prompt[self.lang] = trans

        from efficiency.log import write_dict_to_csv

        write_dict_to_csv([lang2prompt], self.system_prompt_file)
