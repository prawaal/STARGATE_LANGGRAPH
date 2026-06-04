import json

from llm.prompts.prompts import (
    FORWARD_GROWTH_PROMPT
)


class GrowthLLMAnalyzer:

    def __init__(
        self,
        llm_client
    ):

        self.llm = llm_client

    def analyze(
        self,
        company,
        text
    ):

        prompt = (
            FORWARD_GROWTH_PROMPT
            .format(

                company=company,

                text=text[:12000]
            )
        )

        response = self.llm.generate(
            prompt
        )

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            return json.loads(
                response
            )

        except Exception:

            return {

                "ai_demand_acceleration": 0,

                "future_revenue_growth": 0,

                "capacity_scaling": 0,

                "hyperscaler_leverage": 0,

                "long_term_tailwinds": 0,

                "summary":
                    "LLM parsing failed"
            }