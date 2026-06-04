import json

from scoring.financial.financial_data_fetcher import (
    FinancialDataFetcher
)

from scoring.financial.financial_score_calculator import (
    FinancialScoreCalculator
)


# -----------------------------------
# LOAD COMPANY UNIVERSE
# -----------------------------------

with open(

    "outputs/company_universe.json",

    "r",

    encoding="utf-8"

) as f:

    company_data = json.load(f)


company_universe = set()

for category, companies in (
    company_data.items()
):

    for company in companies:

        symbol = company.get(
            "symbol"
        )

        if symbol:

            company_universe.add(
                symbol
            )


company_universe = list(
    company_universe
)


print(
    f"\nLoaded "
    f"{len(company_universe)} "
    f"companies\n"
)


# -----------------------------------
# FETCH FINANCIALS
# -----------------------------------

fetcher = (
    FinancialDataFetcher()
)

raw_metrics = {}

for symbol in (
    company_universe
):

    print(
        f"Fetching financials "
        f"for {symbol}"
    )

    metrics = (
        fetcher.fetch_metrics(
            symbol
        )
    )

    raw_metrics[
        symbol
    ] = metrics


# -----------------------------------
# COMPUTE SCORES
# -----------------------------------

calculator = (
    FinancialScoreCalculator()
)

scores = calculator.compute_scores(
    raw_metrics
)


# -----------------------------------
# SAVE OUTPUT
# -----------------------------------

with open(

    "outputs/financial_scores.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(
        scores,
        f,
        indent=4
    )


print(
    "\nFINANCIAL SCORES GENERATED\n"
)