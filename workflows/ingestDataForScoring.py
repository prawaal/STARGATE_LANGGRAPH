import json

from ingestion.sec.sec_downloader import (
    SECFilingDownloader
)

from ingestion.earnings.earnings_downloader import (
    EarningsDownloader
)

from ingestion.research.acl_title_scraper import (
    ACLTitleScraper
)

from ingestion.sec.sec_url_discovery import (
    SECURLDiscovery
)

from ingestion.earnings.earnings_url_discovery import (
    EarningsURLDiscovery
)

# -----------------------------------
# LOAD COMPANY UNIVERSE
# -----------------------------------

with open(
    "outputs/company_universe.json",
    "r",
    encoding="utf-8"
) as f:

    company_universe = json.load(f)


# -----------------------------------
# INIT DOWNLOADERS
# -----------------------------------

sec_downloader = (
    SECFilingDownloader()
)

earnings_downloader = (
    EarningsDownloader()
)

acl_scraper = ACLTitleScraper()

sec_discovery = (
    SECURLDiscovery()
)

earnings_discovery = (
    EarningsURLDiscovery()
)
"""
# -----------------------------------
# INGEST SEC FILINGS
# -----------------------------------

print(
    "\nINGESTING SEC FILINGS\n"
)

seen = set()

for category, companies in (
    company_universe.items()
):

    for company in companies:

        symbol = company["symbol"]

        if symbol not in seen:

            seen.add(symbol)

            filings = []

            filings.extend(

                sec_discovery
                .get_latest_filings(
                    symbol,
                    "10-K"
                )
            )

            filings.extend(

                sec_discovery
                .get_latest_filings(
                    symbol,
                    "10-Q"
                )
            )

            for filing in filings:

                sec_downloader.download(

                    company=symbol,

                    filing_type=
                        filing["form_type"],

                    filing_date=
                        filing["date"],

                    url=
                        filing["url"]
                )

"""
# -----------------------------------
# INGEST EARNINGS CALLS
# -----------------------------------

"""
print(
    "\nINGESTING EARNINGS CALLS\n"
)


for category, companies in (
    company_universe.items()
):

    for company in companies:

        symbol = company["symbol"]

        transcript_url = (

            earnings_discovery
            .discover_latest_transcript(
                symbol
            )
        )

        if transcript_url:

            earnings_downloader.download(

                company=symbol,

                quarter="latest",

                url=transcript_url
            )

        else:

            print(
                f"No transcript found "
                f"for {symbol}"
            )
"""

with open(
    "configs/earnings_urls.json",
    "r",
    encoding="utf-8"
) as f:

    earnings_urls = json.load(f)

    
for item in earnings_urls:

    earnings_downloader.download(

        company=item["company"],

        quarter=item["quarter"],

        url=item["url"]
    )
           

# -----------------------------------
# INGEST ACL ABSTRACTS
# -----------------------------------

"""
print(
    "\nINGESTING ACL TITLES\n"
)

acl_scraper.scrape_titles(

    "https://aclanthology.org/volumes/2025.acl-long/",

    "acl_long"
)

acl_scraper.scrape_titles(

    "https://aclanthology.org/volumes/2025.acl-short/",

    "acl_short"
)


print(
    "\nALL INGESTION COMPLETE\n"
)
"""