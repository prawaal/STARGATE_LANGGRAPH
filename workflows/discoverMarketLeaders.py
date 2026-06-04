import json

from market.market_leaders import (
    MarketLeadersDiscoverer
)


# LOAD ETF MAPPINGS
with open(
    "outputs/etf_mappings.json",
    "r",
    encoding="utf-8"
) as f:

    etf_mappings = json.load(f)


# BUILD UNIVERSE
builder = MarketLeadersDiscoverer()

company_universe = builder.build(
    etf_mappings
)


# SAVE OUTPUT
with open(
    "outputs/company_universe.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        company_universe,
        f,
        indent=4
    )


print(
    "\nCompany universe saved "
    "to outputs/company_universe.json"
)