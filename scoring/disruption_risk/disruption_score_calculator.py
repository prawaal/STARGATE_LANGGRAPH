class DisruptionScoreCalculator:

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

        signals = signal_results[
            "GLOBAL_DISRUPTION"
        ]

        max_signal = max([

            v

            for k, v in (
                signals.items()
            )

            if not k.startswith("_")
        ])

        keyword_total = 0

        keyword_breakdown = {}

        for signal, value in (
            signals.items()
        ):

            if signal.startswith("_"):
                continue

            normalized = self.normalize(

                value,

                max_signal
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

        llm = llm_results

        llm_values = [

            llm.get(
                "efficient_ai_risk",
                0
            ),

            llm.get(
                "compute_reduction_risk",
                0
            ),

            llm.get(
                "low_power_ai_risk",
                0
            ),

            llm.get(
                "open_source_disruption",
                0
            ),

            llm.get(
                "alternative_paradigm_risk",
                0
            )
        ]

        llm_score = (
            sum(llm_values)
            / 50
        )

        final_score = (

            0.6 * keyword_score

            +

            0.4 * llm_score
        )

        scores["GLOBAL_DISRUPTION"] = {

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

            "disruption_risk_score":
                round(
                    final_score,
                    4
                ),

            "llm_analysis":
                llm
        }

        return scores