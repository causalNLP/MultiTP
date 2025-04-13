import os
import unicodedata

import backoff


def visual_char_count(s):
    return sum(
        1 for c in unicodedata.normalize("NFC", s) if not unicodedata.combining(c)
    )


class GoogleTranslation:
    def __init__(self):
        from efficiency.nlp import Translator

        self.translator = Translator(
            cache_file="data/cache_trans/google_trans_lookup.csv"
        )
        os.makedirs("data/cache_trans", exist_ok=True)

    def back_translate(self, lang, text):
        if lang == "en":
            return text

        @backoff.on_exception(backoff.expo, Exception, max_value=600)
        def func(tt):
            trans = self.translator.translate(
                tt, src_lang=lang, tgt_lang="en", verbose=False
            )
            return trans

        # Split the text into max 3000 characters chunks, but truncate when there is a space
        # to avoid cutting words in half
        chunks = []
        while len(text) > 1000:
            chunk = text[:1000]
            last_space = chunk.rfind(" ")
            chunks.append(chunk[:last_space])
            text = text[last_space:]
        chunks.append(text)

        back_translated_chunks = [func(chunk) for chunk in chunks]
        back_translated_text = "".join(back_translated_chunks)
        return back_translated_text

    def forward_translate(self, lang, text):
        if lang == "en":
            return text

        @backoff.on_exception(backoff.expo, Exception, max_value=600)
        def func(tt):
            trans = self.translator.translate(
                tt, src_lang="en", tgt_lang=lang, verbose=False
            )
            return trans

        # Split the text into max 3000 characters chunks, but truncate when there is a space
        # to avoid cutting words in half
        chunks = []
        while len(text) > 3000:
            chunk = text[:3000]
            last_space = chunk.rfind(" ")
            chunks.append(chunk[:last_space])
            text = text[last_space:]
        chunks.append(text)

        forward_translated_text = [func(chunk) for chunk in chunks]
        forward_translated_text = "".join(forward_translated_text)
        return forward_translated_text

    @property
    def langs(self):
        from googletrans import LANGUAGES

        translateable_langs = []
        for language_code, language_name in LANGUAGES.items():
            translateable_langs.append(language_code)
        return translateable_langs


def get_translator(provider):
    if provider == "google":
        return GoogleTranslation()
    else:
        raise ValueError(f"Unknown provider: {provider}")
