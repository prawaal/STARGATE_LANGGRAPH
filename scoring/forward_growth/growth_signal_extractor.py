import json
import os
import re

from collections import defaultdict

from scoring.forward_growth.growth_keywords import (
    FORWARD_GROWTH_KEYWORDS
)


class GrowthSignalExtractor:

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
                "text",
                "")

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

    def process_company(
        self,
        company
    ):

        earnings_folder = os.path.join(

            "data",
            "earnings",
            company
        )

        combined_text = ""

        if os.path.exists(
            earnings_folder
        ):

            for file in os.listdir(
                earnings_folder
            ):

                if file.endswith(".json"):

                    path = os.path.join(
                        earnings_folder,
                        file
                    )

                    combined_text += (

                        self.load_text(path)
                        + "\n"
                    )

        signals = {}

        for signal_name, keywords in (
            FORWARD_GROWTH_KEYWORDS.items()
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

        self.results[company] = signals

    def process_all(
        self,
        company_universe
    ):

        for company in company_universe:

            self.process_company(
                company
            )

        return self.results