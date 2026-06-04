import json
import os

from ingestion.common.web_utils import (
    fetch_clean_text
)


class SECFilingDownloader:

    def __init__(self):

        self.base_path = (
            "data/sec_filings"
        )

        os.makedirs(
            self.base_path,
            exist_ok=True
        )

    def download(
        self,
        company,
        filing_type,
        filing_date,
        url
    ):

        text = fetch_clean_text(url)

        if not text:

            return

        data = {

            "source_type":
                "sec_filing",

            "company":
                company,

            "filing_type":
                filing_type,

            "date":
                filing_date,

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
            f"{filing_type}_"
            f"{filing_date}.json"
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
            f"Saved SEC filing "
            f"for {company}"
        )