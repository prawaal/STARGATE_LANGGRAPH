class MoatScoreCalculator:

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

        # find max values
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

        # compute normalized scores
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
                    "ecosystem_lockin",
                    0
                ),

                llm.get(
                    "switching_costs",
                    0
                ),

                llm.get(
                    "strategic_importance",
                    0
                ),

                llm.get(
                    "supply_chain_bottleneck",
                    0
                ),

                llm.get(
                    "proprietary_technology",
                    0
                ),

                llm.get(
                    "infrastructure_criticality",
                    0
                )
            ]

            llm_score = (
                sum(llm_values)
                / 60
            )

            final_score = (

                0.6 * keyword_score

                +

                0.4 * llm_score
            )

            scores[company] = {

                "keyword_signals":
                    keyword_breakdown,

                "keyword_score":
                    round(
                        keyword_score,
                        4
                    ),

                "llm_analysis":
                    llm,

                "llm_score":
                    round(
                        llm_score,
                        4
                    ),

                "final_moat_score":
                    round(
                        final_score,
                        4
                    )
            }

        return scores