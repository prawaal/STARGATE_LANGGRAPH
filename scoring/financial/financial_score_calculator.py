class FinancialScoreCalculator:

    def normalize_positive(
        self,
        value,
        max_value
    ):

        if (
            value is None
            or
            max_value == 0
        ):

            return 0

        return value / max_value

    def normalize_negative(
        self,
        value,
        max_value
    ):

        if (
            value is None
            or
            max_value == 0
        ):

            return 0

        return 1 - (
            value / max_value
        )

    def compute_scores(
        self,
        raw_metrics
    ):

        scores = {}

        max_values = {

            "gross_margin": 0,
            "operating_margin": 0,
            "ebitda_margin": 0,
            "revenue_growth": 0,
            "return_on_equity": 0,
            "debt_to_equity": 0
        }

        # -------------------------
        # FIND MAX VALUES
        # -------------------------

        for company, metrics in (
            raw_metrics.items()
        ):

            for metric in (
                max_values.keys()
            ):

                value = metrics.get(
                    metric
                )

                if (
                    value is not None
                    and
                    value > max_values[
                        metric
                    ]
                ):

                    max_values[
                        metric
                    ] = value

        # -------------------------
        # COMPUTE SCORES
        # -------------------------

        for company, metrics in (
            raw_metrics.items()
        ):

            gross_margin_score = (

                self.normalize_positive(

                    metrics.get(
                        "gross_margin"
                    ),

                    max_values[
                        "gross_margin"
                    ]
                )
            )

            operating_margin_score = (

                self.normalize_positive(

                    metrics.get(
                        "operating_margin"
                    ),

                    max_values[
                        "operating_margin"
                    ]
                )
            )

            ebitda_margin_score = (

                self.normalize_positive(

                    metrics.get(
                        "ebitda_margin"
                    ),

                    max_values[
                        "ebitda_margin"
                    ]
                )
            )

            revenue_growth_score = (

                self.normalize_positive(

                    metrics.get(
                        "revenue_growth"
                    ),

                    max_values[
                        "revenue_growth"
                    ]
                )
            )

            roe_score = (

                self.normalize_positive(

                    metrics.get(
                        "return_on_equity"
                    ),

                    max_values[
                        "return_on_equity"
                    ]
                )
            )

            debt_score = (

                self.normalize_negative(

                    metrics.get(
                        "debt_to_equity"
                    ),

                    max_values[
                        "debt_to_equity"
                    ]
                )
            )

            final_score = (

                gross_margin_score
                +
                operating_margin_score
                +
                ebitda_margin_score
                +
                revenue_growth_score
                +
                roe_score
                +
                debt_score
            ) / 6

            scores[company] = {

                "raw_metrics":
                    metrics,

                "financial_quality_score":
                    round(
                        final_score,
                        4
                    )
            }

        return scores