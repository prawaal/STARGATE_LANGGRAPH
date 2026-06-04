import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re


class WebScraper:

    def __init__(self, output_dir="data/raw"):

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def clean_text(self, text):

        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def scrape_url(self, url):

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=20)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script/style tags
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        text = soup.get_text(separator=" ")

        cleaned = self.clean_text(text)

        return cleaned

    def save_text(self, url, text):

        safe_name = (
            url.replace("https://", "")
               .replace("http://", "")
               .replace("/", "_")
               .replace("?", "_")
               .replace("&", "_")
        )

        file_path = self.output_dir / f"{safe_name}.txt"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        return file_path

    def scrape_and_save(self, url):

        print(f"Scraping: {url}")

        text = self.scrape_url(url)

        file_path = self.save_text(url, text)

        print(f"Saved to: {file_path}")

        return file_path