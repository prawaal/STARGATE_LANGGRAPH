import yfinance as yf


class FinancialDataFetcher:

    def fetch_metrics(
        self,
        symbol
    ):

        try:

            ticker = yf.Ticker(
                symbol
            )

            info = ticker.info

            metrics = {

                "gross_margin":
                    info.get(
                        "grossMargins"
                    ),

                "operating_margin":
                    info.get(
                        "operatingMargins"
                    ),

                "ebitda_margin":
                    info.get(
                        "ebitdaMargins"
                    ),

                "revenue_growth":
                    info.get(
                        "revenueGrowth"
                    ),

                "return_on_equity":
                    info.get(
                        "returnOnEquity"
                    ),

                "debt_to_equity":
                    info.get(
                        "debtToEquity"
                    ),

                "free_cashflow":
                    info.get(
                        "freeCashflow"
                    ),

                "market_cap":
                    info.get(
                        "marketCap"
                    )
            }

            return metrics

        except Exception as e:

            print(
                f"Financial fetch failed "
                f"for {symbol}: {e}"
            )

            return {}