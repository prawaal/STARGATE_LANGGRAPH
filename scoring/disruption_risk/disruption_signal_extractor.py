import json
import os
import re

from collections import defaultdict

from scoring.disruption_risk.disruption_keywords import (
    DISRUPTION_KEYWORDS
)


class DisruptionSignalExtractor:

    def __init__(self):

        self.results = defaultdict(dict)

    def load_text(
        self,
        path
    ):

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            return data.get(
                "title",
                ""
            )

        except Exception:

            return ""

    def count_mentions(
        self,
        text,
        keywords
    ):

        text = text.lower()

        count = 0

        for keyword in keywords:

            matches = re.findall(

                re.escape(
                    keyword.lower()
                ),

                text
            )

            count += len(matches)

        return count

    def process_acl_titles(self):

        acl_folder = os.path.join(

            "data",
            "acl_titles"
        )

        combined_text = ""

        if os.path.exists(
            acl_folder
        ):

            for file in os.listdir(
                acl_folder
            ):

                if file.endswith(".json"):

                    path = os.path.join(
                        acl_folder,
                        file
                    )

                    combined_text += (

                        self.load_text(path)
                        + "\n"
                    )

        signals = {}

        for signal_name, keywords in (
            DISRUPTION_KEYWORDS.items()
        ):

            signals[signal_name] = (

                self.count_mentions(

                    combined_text,

                    keywords
                )
            )

        signals["_combined_text"] = (
            combined_text[:20000]
        )

        self.results[
            "GLOBAL_DISRUPTION"
        ] = signals

        return self.results