def country2alpha_2(country):
    try:
        country_code = self.LFM.country2alpha_2[country]
    except:
        import pycountry

        try:
            country_code = pycountry.countries.get(common_name=country).alpha_2.lower()
        except:
            try:
                country_code = pycountry.countries.get(name=country).alpha_2.lower()
            except:
                import pdb

                pdb.set_trace()
    return country_code


def language2alpha_2(language):
    import pycountry

    try:
        alpha_2 = pycountry.languages.get(name=language).alpha_2.lower()
        # [l.name for l in pycountry.languages]
    except:
        try:
            alpha_2 = pycountry.languages.get(name=language).alpha_3.lower()
        except:
            import pdb

            pdb.set_trace()
    return alpha_2


def get_suffix(add_paraphrase, country_code):
    suffix = ""
    if add_paraphrase:
        suffix += "_para"
    if country_code is not None:
        suffix += f"_{country_code}"
    return suffix


def get_model_name_path(model_version):
    return model_version.replace("/", "_")


import ast


def convert_string_to_object(s):
    try:
        return ast.literal_eval(s)
    except:
        return s


# import transformers


class TransformerQuery:
    _llm = None
    _model_version = None

    def __init__(self, model_version, max_tokens, system_prompt=None) -> None:
        self.system_prompt = system_prompt
        self.max_tokens = max_tokens

        import torch
        from vllm import LLM, SamplingParams

        num_gpus = torch.cuda.device_count()

        if TransformerQuery._llm is None:
            TransformerQuery._llm = LLM(
                model_version,
                max_num_seqs=4,
                tensor_parallel_size=num_gpus,
                trust_remote_code=True,
            )
            TransformerQuery._model_version = model_version
        assert model_version == TransformerQuery._model_version
        self.llm = TransformerQuery._llm
        self.sampling_params = SamplingParams(
            max_tokens=max_tokens,
            temperature=0.0,
        )
        self.model_version = model_version
        # self.pipeline = transformers.pipeline(
        #     "text-generation",
        #     model=model_version,
        #     device_map="auto",
        # )

        # # Check that tokenizer has template
        # if self.pipeline.tokenizer.chat_template is None:
        #     raise ValueError("Tokenizer does not have chat template")

    def ask(self, query):
        if self.system_prompt is None:
            messages = [{"role": "user", "content": query}]
        else:
            if "gemma" in self.model_version.lower():
                messages = [
                    {"role": "user", "content": self.system_prompt + "\n" + query},
                ]
            else:
                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": query},
                ]
        # outputs = self.pipeline(
        #     messages,
        #     max_new_tokens=self.max_tokens,
        #     do_sample=False,
        #     top_k=None,
        #     top_p=1.0,
        #     temperature=None,
        # )
        outputs = self.llm.chat(
            messages, sampling_params=self.sampling_params, use_tqdm=False
        )

        # return outputs[0]["generated_text"][-1]["content"]
        return outputs[0].outputs[0].text

    def ask_batch(self, queries):
        from vllm.entrypoints.llm import apply_chat_template, parse_chat_messages

        prompts = []
        for q in queries:
            messages = []
            if self.system_prompt is None:
                messages = [{"role": "user", "content": q}]
            else:
                if "gemma" in self.model_version.lower():
                    messages = [
                        {"role": "user", "content": self.system_prompt + "\n" + q},
                    ]
                else:
                    messages = [
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": q},
                    ]
            tokenizer = self.llm.get_tokenizer()
            model_config = self.llm.llm_engine.get_model_config()
            conversations, _ = parse_chat_messages(messages, model_config, tokenizer)

            prompt = apply_chat_template(
                tokenizer,
                conversations,
                chat_template=None,
                add_generation_prompt=True,
            )
            prompts.append(prompt)

        outputs = self.llm.generate(
            prompts, sampling_params=self.sampling_params, use_tqdm=True
        )
        return [o.outputs[0].text for o in outputs]


def get_llm_model(model_version, max_tokens, system_prompt=None):
    if "gpt" in model_version:
        from efficiency.nlp import AzureChatbot, Chatbot

        if "z-" in model_version:
            return AzureChatbot(model_version, max_tokens, system_prompt=system_prompt)
        return Chatbot(model_version, max_tokens, system_prompt=system_prompt)
    else:
        return TransformerQuery(model_version, max_tokens, system_prompt)


# Translate MultiTP dataset
dataset_file_tmpl = (
    "data/datasets/dataset_{lang}+{translator_provider_forward}{suffix}.csv"
)
system_prompt_file_tmpl = (
    "data/datasets/system_prompt_{role}-{lang}+{translator_provider_forward}.csv"
)
# Back translation of dataset (for analysis)
dataset_back_translated_file_tmpl = "data/datasets/dataset_{lang}+{translator_provider_forward}{suffix}_back_translated.csv"

# Query model
cache_responses_tmpl = "data/cache/{model_version}_{system_role}_{lang}+{translator_provider_forward}{suffix}_raw_resp.csv"

# Back translation
cache_back_responses_tmpl = "data/cache/{model_version}_{system_role}_{lang}+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_resp.csv"

# Parsing
cache_parse_responses_tmpl = "data/cache_parsing/B={analysis_backend_model_version}/{model_version}_{system_role}_{lang}+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_response.csv"

# Performance analsisi
performance_file_tmpl = "data/performance/B={analysis_backend_model_version}/{model_version}_{system_role}_{lang}+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_performance.csv"
performance_file_v2_tmpl = "data/performance/B={analysis_backend_model_version}/{model_version}_{system_role}_{lang}+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_performance_v2.csv"
pivot_file_tmpl = "data/language_results/B={analysis_backend_model_version}/{model_version}_{system_role}_LANGs+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_pivot.csv"
pivot_file_by_country_tmpl = "data/language_results/B={analysis_backend_model_version}/{model_version}_{system_role}_COUNTRIES+{translator_provider_forward}{suffix}_tr+{translator_provider_backward}_pivot.csv"

LANGUAGES = [
    "af",
    "am",
    "ar",
    "az",
    "be",
    "bg",
    "bn",
    "bs",
    "ca",
    "ceb",
    "co",
    "cs",
    "cy",
    "da",
    "de",
    "el",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "fy",
    "ga",
    "gd",
    "gl",
    "gu",
    "ha",
    "haw",
    "he",
    "hi",
    "hmn",
    "hr",
    "ht",
    "hu",
    "hy",
    "id",
    "ig",
    "is",
    "it",
    "iw",
    "ja",
    "jw",
    "ka",
    "kk",
    "km",
    "kn",
    "ko",
    "ku",
    "ky",
    "la",
    "lb",
    "lo",
    "lt",
    "lv",
    "mg",
    "mi",
    "mk",
    "ml",
    "mn",
    "mr",
    "ms",
    "mt",
    "my",
    "ne",
    "nl",
    "no",
    "ny",
    "or",
    "pa",
    "pl",
    "ps",
    "pt",
    "ro",
    "ru",
    "sd",
    "si",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sq",
    "sr",
    "st",
    "su",
    "sv",
    "sw",
    "ta",
    "te",
    "tg",
    "th",
    "tl",
    "tr",
    "ug",
    "uk",
    "ur",
    "uz",
    "vi",
    "xh",
    "yi",
    "yo",
    "zh-cn",
    "zh-tw",
    "zu",
]


COUNTRIES = [
    "abw",
    "afg",
    "ago",
    "aia",
    "ala",
    "alb",
    "and",
    "are",
    "arg",
    "arm",
    "asm",
    "ata",
    "atf",
    "atg",
    "aus",
    "aut",
    "aze",
    "bdi",
    "bel",
    "ben",
    "bes",
    "bfa",
    "bgd",
    "bgr",
    "bhr",
    "bhs",
    "bih",
    "blm",
    "blr",
    "blz",
    "bmu",
    "bol",
    "bra",
    "brb",
    "brn",
    "btn",
    "bvt",
    "bwa",
    "caf",
    "can",
    "cck",
    "che",
    "chl",
    "chn",
    "civ",
    "cmr",
    "cod",
    "cog",
    "cok",
    "col",
    "com",
    "cpv",
    "cri",
    "cub",
    "cuw",
    "cxr",
    "cym",
    "cyp",
    "cze",
    "deu",
    "dji",
    "dma",
    "dnk",
    "dom",
    "dza",
    "ecu",
    "egy",
    "eri",
    "esh",
    "esp",
    "est",
    "eth",
    "fin",
    "fji",
    "flk",
    "fra",
    "fro",
    "fsm",
    "gab",
    "gbr",
    "geo",
    "ggy",
    "gha",
    "gib",
    "gin",
    "glp",
    "gmb",
    "gnb",
    "gnq",
    "grc",
    "grd",
    "grl",
    "gtm",
    "guf",
    "gum",
    "guy",
    "hkg",
    "hmd",
    "hnd",
    "hrv",
    "hti",
    "hun",
    "idn",
    "imn",
    "ind",
    "iot",
    "irl",
    "irn",
    "irq",
    "isl",
    "isr",
    "ita",
    "jam",
    "jey",
    "jor",
    "jpn",
    "kaz",
    "ken",
    "kgz",
    "khm",
    "kir",
    "kna",
    "kor",
    "kwt",
    "lao",
    "lbn",
    "lbr",
    "lby",
    "lca",
    "lie",
    "lka",
    "lso",
    "ltu",
    "lux",
    "lva",
    "mac",
    "maf",
    "mar",
    "mco",
    "mda",
    "mdg",
    "mdv",
    "mex",
    "mhl",
    "mkd",
    "mli",
    "mlt",
    "mmr",
    "mne",
    "mng",
    "mnp",
    "moz",
    "mrt",
    "msr",
    "mtq",
    "mus",
    "mwi",
    "mys",
    "myt",
    "nam",
    "ncl",
    "ner",
    "nfk",
    "nga",
    "nic",
    "niu",
    "nld",
    "nor",
    "npl",
    "nru",
    "nzl",
    "omn",
    "pak",
    "pan",
    "pcn",
    "per",
    "phl",
    "plw",
    "png",
    "pol",
    "pri",
    "prk",
    "prt",
    "pry",
    "pse",
    "pyf",
    "qat",
    "reu",
    "rou",
    "rus",
    "rwa",
    "sau",
    "sdn",
    "sen",
    "sgp",
    "sgs",
    "shn",
    "sjm",
    "slb",
    "sle",
    "slv",
    "smr",
    "som",
    "spm",
    "srb",
    "ssd",
    "stp",
    "sur",
    "svk",
    "svn",
    "swe",
    "swz",
    "sxm",
    "syc",
    "syr",
    "tca",
    "tcd",
    "tgo",
    "tha",
    "tjk",
    "tkl",
    "tkm",
    "tls",
    "ton",
    "tto",
    "tun",
    "tur",
    "tuv",
    "twn",
    "tza",
    "uga",
    "ukr",
    "umi",
    "ury",
    "usa",
    "uzb",
    "vat",
    "vct",
    "ven",
    "vgb",
    "vir",
    "vnm",
    "vut",
    "wlf",
    "wsm",
    "yem",
    "zaf",
    "zmb",
    "zwe",
]
