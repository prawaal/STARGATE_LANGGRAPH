import math


DISRUPTION_MULTIPLIERS = {

    "Compute Infrastructure": 1.0,

    "Semiconductor Supply Chain": 0.9,

    "Network Infrastructure": 0.6,

    "Power Infrastructure": 0.3,

    "Cooling Infrastructure": 0.4,

    "Physical Infrastructure": 0.2,

    "AI Operations & Services": 0.7
}


class AIFactoryScoreCalculator:

    def safe_score(
        self,
        value
    ):

        if value is None:
            return 0.05

        return max(
            value,
            0.05
        )

    def compute_final_score(

        self,

        moat_score,

        financial_score,

        ai_exposure_score,

        forward_growth_score,

        disruption_risk,

        disruption_multiplier
    ):

        # -----------------------------------
        # SAFE SCORES
        # -----------------------------------

        moat_score = self.safe_score(
            moat_score
        )

        financial_score = self.safe_score(
            financial_score
        )

        ai_exposure_score = self.safe_score(
            ai_exposure_score
        )

        forward_growth_score = self.safe_score(
            forward_growth_score
        )

        # -----------------------------------
        # STRUCTURAL ADVANTAGE
        # -----------------------------------

        structural_advantage = math.sqrt(

            moat_score

            *

            financial_score
        )

        # -----------------------------------
        # CORE GROWTH SCORE
        # -----------------------------------

        core_growth_score = (

            structural_advantage

            *

            ai_exposure_score

            *

            forward_growth_score

        ) ** (1/3)

        # -----------------------------------
        # DISRUPTION ADJUSTMENT
        # -----------------------------------

        effective_disruption = (

            disruption_risk

            *

            disruption_multiplier
        )

        final_score = (

            core_growth_score

            *

            (
                1
                -
                effective_disruption
            )
        )

        return {

            "structural_advantage":
                round(
                    structural_advantage,
                    4
                ),

            "core_growth_score":
                round(
                    core_growth_score,
                    4
                ),

            "effective_disruption":
                round(
                    effective_disruption,
                    4
                ),

            "final_score":
                round(
                    final_score,
                    4
                )
        }