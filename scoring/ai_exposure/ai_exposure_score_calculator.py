class AIExposureScoreCalculator:

    def normalize(
        self,
        value,
        max_value
    ):

        if max_value == 0:
            return 0

        return value / max_value

    def compute_scores(
        self,
        signal_results,
        llm_results
    ):

        scores = {}

        max_scores = {}

        for company, signals in (
            signal_results.items()
        ):

            for signal, value in (
                signals.items()
            ):

                if signal.startswith("_"):
                    continue

                current = max_scores.get(
                    signal,
                    0
                )

                if value > current:

                    max_scores[
                        signal
                    ] = value

        for company, signals in (
            signal_results.items()
        ):

            keyword_total = 0

            keyword_breakdown = {}

            for signal, value in (
                signals.items()
            ):

                if signal.startswith("_"):
                    continue

                normalized = self.normalize(

                    value,

                    max_scores[
                        signal
                    ]
                )

                keyword_breakdown[
                    signal
                ] = round(
                    normalized,
                    4
                )

                keyword_total += normalized

            keyword_score = (

                keyword_total
                /
                len(keyword_breakdown)
            )

            llm = llm_results.get(
                company,
                {}
            )

            llm_values = [

                llm.get(
                    "ai_revenue_exposure",
                    0
                ),

                llm.get(
                    "hyperscaler_dependency",
                    0
                ),

                llm.get(
                    "future_ai_growth",
                    0
                ),

                llm.get(
                    "capacity_scaling",
                    0
                )
            ]

            llm_score = (
                sum(llm_values)
                / 40
            )

            final_score = (

                0.6 * keyword_score

                +

                0.4 * llm_score
            )

            scores[company] = {

                "keyword_score":
                    round(
                        keyword_score,
                        4
                    ),

                "llm_score":
                    round(
                        llm_score,
                        4
                    ),

                "final_ai_exposure_score":
                    round(
                        final_score,
                        4
                    ),

                "llm_analysis":
                    llm
            }

        return scores