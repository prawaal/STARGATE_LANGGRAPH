import json

from scoring.final_ranking.ai_factory_score_calculator import (

    AIFactoryScoreCalculator,

    DISRUPTION_MULTIPLIERS
)


# -----------------------------------
# LOAD ALL SCORES
# -----------------------------------

seen_symbols = set()

with open(

    "outputs/company_universe.json",

    "r",

    encoding="utf-8"

) as f:

    company_universe = json.load(f)


with open(

    "outputs/moat_scores.json",

    "r",

    encoding="utf-8"

) as f:

    moat_scores = json.load(f)


with open(

    "outputs/financial_scores.json",

    "r",

    encoding="utf-8"

) as f:

    financial_scores = json.load(f)


with open(

    "outputs/ai_exposure_scores.json",

    "r",

    encoding="utf-8"

) as f:

    ai_exposure_scores = json.load(f)


with open(

    "outputs/forward_growth_scores.json",

    "r",

    encoding="utf-8"

) as f:

    growth_scores = json.load(f)


with open(

    "outputs/disruption_risk_scores.json",

    "r",

    encoding="utf-8"

) as f:

    disruption_scores = json.load(f)


# -----------------------------------
# GLOBAL DISRUPTION SCORE
# -----------------------------------

global_disruption = (

    disruption_scores[
        "GLOBAL_DISRUPTION"
    ][
        "disruption_risk_score"
    ]
)


# -----------------------------------
# INIT CALCULATOR
# -----------------------------------

calculator = (
    AIFactoryScoreCalculator()
)


# -----------------------------------
# COMPUTE FINAL SCORES
# -----------------------------------

final_rankings = []

for category, companies in (
    company_universe.items()
):

    disruption_multiplier = (

        DISRUPTION_MULTIPLIERS.get(

            category,

            0.5
        )
    )

    for company in companies:

        symbol = company.get(
            "symbol"
        )

        moat_score = (

            moat_scores.get(

                symbol,

                {}
            ).get(

                "final_moat_score",

                0.05
            )
        )

        financial_score = (

            financial_scores.get(

                symbol,

                {}
            ).get(

                "financial_quality_score",

                0.05
            )
        )

        ai_exposure_score = (

            ai_exposure_scores.get(

                symbol,

                {}
            ).get(

                "final_ai_exposure_score",

                0.05
            )
        )

        forward_growth_score = (

            growth_scores.get(

                symbol,

                {}
            ).get(

                "forward_growth_score",

                0.05
            )
        )

        result = (

            calculator.compute_final_score(

                moat_score,

                financial_score,

                ai_exposure_score,

                forward_growth_score,

                global_disruption,

                disruption_multiplier
            )
        )

        # -----------------------------------
        # SKIP DUPLICATES
        # -----------------------------------

        if symbol in seen_symbols:

            continue


        seen_symbols.add(
            symbol
        )

        final_rankings.append({

            "symbol": symbol,

            "company_name":
                company.get(
                    "company_name"
                ),

            "category":
                category,

            "moat_score":
                moat_score,

            "financial_score":
                financial_score,

            "ai_exposure_score":
                ai_exposure_score,

            "forward_growth_score":
                forward_growth_score,

            "disruption_multiplier":
                disruption_multiplier,

            **result
        })


# -----------------------------------
# SORT FINAL SCORES
# -----------------------------------

final_rankings = sorted(

    final_rankings,

    key=lambda x:
        x["final_score"],

    reverse=True
)


# -----------------------------------
# SAVE OUTPUT
# -----------------------------------

with open(

    "outputs/final_ai_factory_rankings.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        final_rankings,

        f,

        indent=4
    )


# -----------------------------------
# PRINT TOP 20
# -----------------------------------

print(
    "\nTOP AI FACTORY "
    "COMPANIES\n"
)

for i, company in enumerate(

    final_rankings[:20],

    start=1
):

    print(

        f"{i}. "

        f"{company['company_name']} "

        f"({company['category']}) "

        f"-> "

        f"{company['final_score']}"
    )


print(
    "\nFINAL AI FACTORY "
    "RANKINGS GENERATED\n"
)