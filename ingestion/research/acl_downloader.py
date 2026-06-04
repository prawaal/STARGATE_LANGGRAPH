import json
import os
import requests

from bs4 import BeautifulSoup


class ACLDownloader:

    def __init__(self):

        self.base_path = (
            "data/research/ACL"
        )

        os.makedirs(
            self.base_path,
            exist_ok=True
        )

    def download_paper(
        self,
        paper_url
    ):

        try:

            response = requests.get(
                paper_url,
                timeout=20
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            title = soup.find("h2")

            abstract = soup.find(
                "div",
                class_="acl-abstract"
            )

            data = {

                "source_type":
                    "research_abstract",

                "conference":
                    "ACL",

                "url":
                    paper_url,

                "title":
                    title.text.strip()
                    if title else "",

                "abstract":
                    abstract.text.strip()
                    if abstract else ""
            }

            safe_title = (
                data["title"]
                .replace("/", "_")
                [:80]
            )

            output_path = (
                f"{self.base_path}/"
                f"{safe_title}.json"
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
                f"Saved ACL paper: "
                f"{safe_title}"
            )

        except Exception as e:

            print(
                f"ACL download error: {e}"
            )