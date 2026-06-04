import json

from llm.prompts.prompts import (
    AI_EXPOSURE_PROMPT
)


class AIExposureLLMAnalyzer:

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
            AI_EXPOSURE_PROMPT
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

                "ai_revenue_exposure": 0,

                "hyperscaler_dependency": 0,

                "future_ai_growth": 0,

                "capacity_scaling": 0,

                "summary":
                    "LLM parsing failed"
            }