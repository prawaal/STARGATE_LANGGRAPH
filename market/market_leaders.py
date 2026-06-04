from collections import defaultdict

from market.etf_holdings import (
    ETFHoldingsFetcher
)


class MarketLeadersDiscoverer:

    def __init__(self):

        self.fetcher = (
            ETFHoldingsFetcher()
        )

    def build(
        self,
        etf_mappings
    ):

        universe = defaultdict(dict)

        for mapping in etf_mappings:

            category = mapping["category"]

            print(
                f"\nProcessing: {category}"
            )

            category_companies = {}

            for etf in mapping["etfs"]:

                ticker = etf["ticker"]

                print(
                    f"Fetching holdings: "
                    f"{ticker}"
                )

                holdings = (
                    self.fetcher.fetch_holdings(
                        ticker
                    )
                )

                for company in holdings:

                    symbol = (
                        company["symbol"]
                    )

                    weight = (
                        company[
                            "holding_percent"
                        ]
                    )

                    if (
                        symbol
                        not in category_companies
                    ):

                        category_companies[symbol] = {

                            "category": category,

                            "symbol": symbol,

                            "company_name": company[
                                "company_name"
                            ],

                            "source_etfs": [
                                ticker
                            ],

                            "combined_weight": weight
                        }

                    else:

                        category_companies[
                            symbol
                        ][
                            "combined_weight"
                        ] += weight

                        category_companies[
                            symbol
                        ][
                            "source_etfs"
                        ].append(
                            ticker
                        )

            sorted_companies = sorted(

                category_companies.values(),

                key=lambda x: (
                    x["combined_weight"]
                ),

                reverse=True
            )

            universe[category] = (
                sorted_companies[:30]
            )

        return universe