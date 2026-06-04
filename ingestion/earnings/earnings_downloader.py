import json
import os

from ingestion.common.web_utils import (
    fetch_clean_text
)


class EarningsDownloader:

    def __init__(self):

        self.base_path = (
            "data/earnings"
        )

        os.makedirs(
            self.base_path,
            exist_ok=True
        )

    def download(
        self,
        company,
        url,
        quarter="latest"
    ):

        text = fetch_clean_text(url)

        if not text:

            return

        data = {

            "source_type":
                "earnings_call",

            "company":
                company,

            "quarter":
                quarter,

            "url":
                url,

            "text":
                text
        }

        folder = (
            f"{self.base_path}/"
            f"{company}"
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

        output_path = (
            f"{folder}/"
            f"{quarter}.json"
        )

        with open(

            output_path,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

        print(
            f"Saved earnings call "
            f"for {company}"
        )