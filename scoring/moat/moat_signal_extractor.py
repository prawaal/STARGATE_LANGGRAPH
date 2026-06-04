import json
import os
import re

from collections import defaultdict

from scoring.moat.moat_keywords import (
    MOAT_KEYWORDS
)


class MoatSignalExtractor:

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
                ""
            )

        except Exception:

            return ""

    def count_keyword_mentions(
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

    def collect_company_text(
        self,
        company
    ):

        combined_text = ""

        source_count = 0

        # -----------------------------
        # EARNINGS
        # -----------------------------

        earnings_folder = os.path.join(

            "data",
            "earnings",
            company
        )

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

            source_count += 1

        # -----------------------------
        # SEC
        # -----------------------------

        sec_folder = os.path.join(

            "data",
            "sec",
            company
        )

        if os.path.exists(
            sec_folder
        ):

            for root, dirs, files in os.walk(
                sec_folder
            ):

                for file in files:

                    if file.endswith(
                        ".json"
                    ):

                        path = os.path.join(
                            root,
                            file
                        )

                        combined_text += (

                            self.load_text(path)
                            + "\n"
                        )

            source_count += 1

        return (

            combined_text,

            source_count
        )

    def process_company(
        self,
        company
    ):

        combined_text, source_count = (

            self.collect_company_text(
                company
            )
        )

        signals = {}

        for signal_name, keywords in (
            MOAT_KEYWORDS.items()
        ):

            raw_count = (

                self.count_keyword_mentions(

                    combined_text,

                    keywords
                )
            )

            # normalize by available sources
            normalized_count = (

                raw_count
                /
                max(source_count, 1)
            )

            signals[signal_name] = round(

                normalized_count,

                2
            )

        signals["_combined_text"] = (
            combined_text[:20000]
        )

        signals["_source_count"] = (
            source_count
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