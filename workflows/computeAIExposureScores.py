import json

from llm.llm_factory import (
    LLMFactory
)

from scoring.ai_exposure.ai_exposure_signal_extractor import (
    AIExposureSignalExtractor
)

from scoring.ai_exposure.ai_exposure_llm_analyzer import (
    AIExposureLLMAnalyzer
)

from scoring.ai_exposure.ai_exposure_score_calculator import (
    AIExposureScoreCalculator
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
# INIT COMPONENTS
# -----------------------------------

llm_client = (
    LLMFactory.create_llm()
)

extractor = (
    AIExposureSignalExtractor()
)

llm_analyzer = (
    AIExposureLLMAnalyzer(
        llm_client
    )
)

calculator = (
    AIExposureScoreCalculator()
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
        f"Running AI exposure "
        f"analysis for {company}"
    )

    combined_text = signals.get(
        "_combined_text",
        ""
    )

    # skip if insufficient text
    if len(combined_text) < 500:

        print(
            f"Skipping {company} "
            f"(insufficient text)"
        )

        continue

    llm_results[company] = (

        llm_analyzer.analyze(

            company,

            combined_text
        )
    )


# -----------------------------------
# COMPUTE FINAL SCORES
# -----------------------------------

scores = calculator.compute_scores(

    signal_results,

    llm_results
)


# -----------------------------------
# SAVE OUTPUT
# -----------------------------------

with open(

    "outputs/ai_exposure_scores.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(
        scores,
        f,
        indent=4
    )


print(
    "\nAI EXPOSURE SCORES GENERATED\n"
)