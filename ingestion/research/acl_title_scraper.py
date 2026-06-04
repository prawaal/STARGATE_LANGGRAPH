import json
import os
import requests

from bs4 import BeautifulSoup


class ACLTitleScraper:

    def __init__(self):

        self.base_path = (
            "data/research/ACL"
        )

        os.makedirs(
            self.base_path,
            exist_ok=True
        )

    def scrape_titles(
        self,
        url,
        track_name
    ):

        try:

            response = requests.get(

                url,

                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                },

                timeout=20
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            with open(
                "acl_debug.html",
                "w",
                encoding="utf-8"
            ) as f:

                f.write(
                    soup.prettify()
                )

            print("Saved debug HTML")

            papers = []

            title_tags = soup.find_all("strong")

            for tag in title_tags:

                title = tag.get_text(
                    strip=True
                )

                # remove proceedings heading
                if (
                    "Proceedings of"
                    in title
                ):
                    continue

                # remove tiny/noisy tags
                if len(title) < 15:
                    continue

                papers.append({

                    "conference":
                        "ACL",

                    "track":
                        track_name,

                    "title":
                        title
                })

            output_path = (

                f"{self.base_path}/"
                f"{track_name}_titles.json"
            )

            with open(

                output_path,

                "w",

                encoding="utf-8"

            ) as f:

                json.dump(
                    papers,
                    f,
                    indent=4
                )

            print(

                f"Saved {len(papers)} "
                f"titles for {track_name}"
            )

        except Exception as e:

            print(
                f"ACL scraping error: {e}"
            )