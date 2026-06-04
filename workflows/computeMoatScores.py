import json

from llm.llm_factory import (
    LLMFactory
)

from scoring.moat.moat_signal_extractor import (
    MoatSignalExtractor
)

from scoring.moat.moat_llm_analyzer import (
    MoatLLMAnalyzer
)

from scoring.moat.moat_score_calculator import (
    MoatScoreCalculator
)


# -----------------------------------
# INIT
# -----------------------------------

llm_client = (
    LLMFactory.create_llm()
)

extractor = (
    MoatSignalExtractor()
)

llm_analyzer = (
    MoatLLMAnalyzer(
        llm_client
    )
)

calculator = (
    MoatScoreCalculator()
)


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
# EXTRACT KEYWORD SIGNALS
# -----------------------------------

signal_results = extractor.process_all(
    company_universe
)


# -----------------------------------
# RUN LLM ANALYSIS
# -----------------------------------

llm_results = {}

for company, signals in (
    signal_results.items()
):

    print(
        f"Running moat analysis "
        f"for {company}"
    )

    llm_results[company] = (

        llm_analyzer.analyze(

            company,

            signals["_combined_text"]
        )
    )


# -----------------------------------
# COMPUTE SCORES
# -----------------------------------

scores = calculator.compute_scores(

    signal_results,

    llm_results
)


# -----------------------------------
# SAVE OUTPUT
# -----------------------------------

with open(

    "outputs/moat_scores.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(
        scores,
        f,
        indent=4
    )


print(
    "\nMOAT SCORES GENERATED\n"
)