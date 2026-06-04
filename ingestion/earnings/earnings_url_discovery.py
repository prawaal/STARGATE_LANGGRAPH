import requests
from bs4 import BeautifulSoup


class EarningsURLDiscovery:

    def __init__(self):

        self.headers = {

            "User-Agent":
                "Mozilla/5.0"
        }

    def discover_latest_transcript(
        self,
        ticker
    ):

        try:

            query = (
                f"{ticker} earnings call "
                f"transcript Seeking Alpha"
            )

            search_url = (

                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )

            response = requests.get(

                search_url,

                headers=self.headers,

                timeout=20
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            links = soup.find_all("a")

            for link in links:

                href = link.get("href")

                if not href:

                    continue

                if (
                    "seekingalpha.com"
                    in href
                    and
                    "earnings-call-transcript"
                    in href
                ):

                    if href.startswith("/url?q="):

                        clean = (
                            href.split("/url?q=")[1]
                            .split("&")[0]
                        )

                        return clean

            return None

        except Exception as e:

            print(
                f"Earnings discovery "
                f"failed for {ticker}: {e}"
            )

            return None