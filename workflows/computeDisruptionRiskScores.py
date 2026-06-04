import json

from llm.llm_factory import (
    LLMFactory
)

from scoring.disruption_risk.disruption_signal_extractor import (
    DisruptionSignalExtractor
)

from scoring.disruption_risk.disruption_llm_analyzer import (
    DisruptionLLMAnalyzer
)

from scoring.disruption_risk.disruption_score_calculator import (
    DisruptionScoreCalculator
)


# -----------------------------------
# INIT COMPONENTS
# -----------------------------------

llm_client = (
    LLMFactory.create_llm()
)

extractor = (
    DisruptionSignalExtractor()
)

llm_analyzer = (
    DisruptionLLMAnalyzer(
        llm_client
    )
)

calculator = (
    DisruptionScoreCalculator()
)


# -----------------------------------
# EXTRACT SIGNALS
# -----------------------------------

signal_results = (
    extractor.process_acl_titles()
)

combined_text = (

    signal_results[
        "GLOBAL_DISRUPTION"
    ].get(

        "_combined_text",

        ""
    )
)


# -----------------------------------
# RUN LLM ANALYSIS
# -----------------------------------

print(
    "Running disruption "
    "risk analysis"
)

llm_results = (

    llm_analyzer.analyze(
        combined_text
    )
)


# -----------------------------------
# COMPUTE FINAL SCORE
# -----------------------------------

scores = calculator.compute_scores(

    signal_results,

    llm_results
)


# -----------------------------------
# SAVE OUTPUT
# -----------------------------------

with open(

    "outputs/disruption_risk_scores.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(
        scores,
        f,
        indent=4
    )


print(
    "\nDISRUPTION RISK "
    "SCORES GENERATED\n"
)