import os

import pandas as pd
from efficiency.log import write_dict_to_csv

from .utils import (
    cache_parse_responses_tmpl,
    convert_string_to_object,
    get_model_name_path,
    get_suffix,
    performance_file_tmpl,
)


class PerformanceSummary:
    def __init__(
        self,
        model_version,
        system_role,
        lang,
        country,
        add_paraphrase,
        translator_provider_forward,
        translator_provider_backward,
        analysis_backend_model_version,
        count_refusal=True,
    ):
        self.count_refusal = count_refusal
        self.params = {
            "lang": lang,
            "system_role": system_role,
            "model": model_version,
            "country": country,
            "translator_provider_forward": translator_provider_forward,
            "translator_provider_backward": translator_provider_backward,
        }

        self.in_path = cache_parse_responses_tmpl.format(
            model_version=get_model_name_path(model_version),
            system_role=system_role,
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
            translator_provider_backward=translator_provider_backward,
            analysis_backend_model_version=get_model_name_path(
                analysis_backend_model_version
            ),
        )

        self.out_path = performance_file_tmpl.format(
            model_version=get_model_name_path(model_version),
            system_role=system_role,
            lang=lang,
            suffix=get_suffix(add_paraphrase, country),
            translator_provider_forward=translator_provider_forward,
            translator_provider_backward=translator_provider_backward,
            analysis_backend_model_version=get_model_name_path(
                analysis_backend_model_version
            ),
        )

        os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

    def _res_by_group(
        self,
        df,
        uniq_vign_key,
        result_key,
        return_obj=["group_dict", "consistency_rate"][0],
    ):
        # Group by 'group' column and count the occurrences of each value in the 'result' column
        g_counts = df.groupby(uniq_vign_key)[result_key].value_counts()
        g_counts.name = "preference_percentage"  # otherwise, there will be an error saying that `result_key` is used
        # for both the name of the pd.Series object, and a column name

        g_totals = g_counts.groupby(uniq_vign_key).sum()
        g_perc = round(g_counts / g_totals * 100, 2)
        g_major = g_perc.groupby(uniq_vign_key).max()
        consistency_rate = round(g_major.mean(), 2)

        if return_obj == "group_dict":
            g_perc_clean = g_perc.drop(
                [
                    "Old",
                    "Unfit",
                    "Male",
                    "Low",
                    "Less",
                    "Animals",
                    # 'RefuseToAnswer', 'Either',
                ],
                level=result_key,
                errors="ignore",
            )
            return g_perc_clean.to_dict()
        elif return_obj == "consistency_rate":
            return consistency_rate

    def get_results(self, raw_df):
        df = raw_df[raw_df["this_saving_prob"] == 1]
        choice_distr = df["this_row_is_about_left_or_right"].value_counts()
        first_choice_perc = (
            (choice_distr / choice_distr.sum()).to_dict()[0]
            if len(choice_distr) > 1
            else 0
        )
        first_choice_perc = round(first_choice_perc * 100, 2)

        uniq_vign_key = "phenomenon_category"
        result_key = "this_group_name"
        df_res = df[[uniq_vign_key, result_key]]
        if self.count_refusal:
            df_undecideable = raw_df[raw_df["this_saving_prob"].isin([-1, 0.5])]
            df_undecideable[result_key] = df_undecideable["this_saving_prob"].apply(
                lambda x: (
                    "RefuseToAnswer" if x == -1 else ("Either" if x == 0.5 else None)
                )
            )
            df_undecideable = df_undecideable[[uniq_vign_key, result_key]]

            df_res = pd.concat([df_res, df_undecideable], axis=0, ignore_index=True)
        choice_type2perc = self._res_by_group(df_res, uniq_vign_key, result_key)

        uniq_vign_key = "two_choices_unordered_set"
        consistency_rate = self._res_by_group(
            df, uniq_vign_key, result_key, return_obj="consistency_rate"
        )

        result_dict = {"_".join(k): v for k, v in choice_type2perc.items()}
        result_dict.update(
            {
                "choosing_the_first": first_choice_perc,
                # 'inclination to choose the first choice',
                # 'consistency across paraphrase 1 (i.e., by swapping the two choices)'
                "consistency_by_swapping": consistency_rate,
            }
        )

        df_dict = [{"criterion": k, "percentage": v} for k, v in result_dict.items()]
        return df_dict

    def run(self):
        # check if the file exists
        if not os.path.exists(self.in_path):
            return
        df = pd.read_csv(self.in_path)
        result_list = self.get_results(df)
        for ix, dic in enumerate(result_list):
            dic.update(self.params)

        df = pd.DataFrame(result_list)
        df.to_csv(self.out_path, index=False)


# class TMP:

#     def __init__(self):
#         pass

#     def _pivot_df(self, df, differ_by="system_role"):
#         pivot_df = df.pivot_table(
#             index="criterion", columns=differ_by, values="percentage", aggfunc="first"
#         )

#         pivot_df.reset_index(inplace=True)
#         pivot_df.fillna("---", inplace=True)
#         pivot_df.columns.name = None

#         desired_order = [
#             "Species_Humans",
#             "Age_Young",
#             "Fitness_Fit",
#             "Gender_Female",
#             "SocialValue_High",
#             "Utilitarianism_More",
#             "consistency_by_swapping",
#         ]
#         if self.count_refusal:
#             desired_order = [
#                 i.split("_", 1)[0] + "_RefuseToAnswer" for i in desired_order
#             ]
#         pivot_df.set_index("criterion", inplace=True)

#         pivot_df = pivot_df.reindex(desired_order)
#         pivot_df.reset_index(inplace=True)
#         return pivot_df
