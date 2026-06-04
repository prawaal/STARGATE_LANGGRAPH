import requests


class SECURLDiscovery:

    def __init__(self):

        self.headers = {

            "User-Agent":
                "PrawaalResearch prawaal@gmail.com"
        }

    def get_cik(self, ticker):

        url = (
            "https://www.sec.gov/files/"
            "company_tickers.json"
        )

        response = requests.get(

            url,

            headers=self.headers
        )

        companies = response.json()

        ticker = ticker.upper()

        for _, company in companies.items():

            if company["ticker"] == ticker:

                cik = str(
                    company["cik_str"]
                ).zfill(10)

                return cik

        return None
    
    def get_latest_filings(
        self,
        ticker,
        form_type="10-K",
        limit=1
        ):

        cik = self.get_cik(ticker)

        if not cik:

            return []

        submissions_url = (

            f"https://data.sec.gov/"
            f"submissions/CIK{cik}.json"
        )

        response = requests.get(

            submissions_url,

            headers=self.headers
        )

        data = response.json()

        recent = (
            data["filings"]["recent"]
        )

        filings = []

        forms = recent["form"]

        accession_numbers = (
            recent["accessionNumber"]
        )

        primary_docs = (
            recent["primaryDocument"]
        )

        filing_dates = (
            recent["filingDate"]
        )

        for i in range(len(forms)):

            if forms[i] == form_type:

                accession = (
                    accession_numbers[i]
                    .replace("-", "")
                )

                primary_doc = (
                    primary_docs[i]
                )

                filing_url = (

                    f"https://www.sec.gov/"
                    f"Archives/edgar/data/"
                    f"{int(cik)}/"
                    f"{accession}/"
                    f"{primary_doc}"
                )

                filings.append({

                    "ticker": ticker,

                    "form_type": form_type,

                    "date":
                        filing_dates[i],

                    "url":
                        filing_url
                })

                if len(filings) >= limit:

                    break

        return filings