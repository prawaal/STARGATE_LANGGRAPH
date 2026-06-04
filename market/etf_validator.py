import yfinance as yf


class ETFValidator:

    def __init__(self):

        pass

    def validate_etf(self, ticker):

        try:

            etf = yf.Ticker(ticker)

            info = etf.info

            if not info:
                return False

            quote_type = (
                info.get("quoteType", "")
            )

            return (
                quote_type.lower() == "etf"
            )

        except Exception:

            return False