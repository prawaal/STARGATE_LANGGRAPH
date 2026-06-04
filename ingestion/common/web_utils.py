import requests

from bs4 import BeautifulSoup


def fetch_clean_text(url):

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

        for tag in soup([
            "script",
            "style",
            "nav",
            "footer"
        ]):

            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text

    except Exception as e:

        print(
            f"Error fetching {url}: {e}"
        )

        return None