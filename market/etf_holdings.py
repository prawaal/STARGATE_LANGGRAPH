import yfinance as yf


class ETFHoldingsFetcher:

    def __init__(self):

        pass

    def fetch_holdings(
        self,
        etf_ticker,
        top_n=25
    ):

        try:

            etf = yf.Ticker(etf_ticker)

            holdings = (
                etf.funds_data.top_holdings
            )

            #print(holdings.columns)
            #print(holdings.head())

            if holdings is None:

                return []

            holdings = holdings.head(top_n)

            companies = []

            for symbol, row in holdings.iterrows():

                companies.append({

                    "symbol": symbol,

                    "company_name": row["Name"],

                    "holding_percent": float(
                        row["Holding Percent"]
                    )
                })

            return companies

        except Exception as e:

            print(
                f"Error fetching "
                f"{etf_ticker}: {e}"
            )

            return []