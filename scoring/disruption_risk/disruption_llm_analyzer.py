import json

from llm.prompts.prompts import (
    DISRUPTION_RISK_PROMPT
)


class DisruptionLLMAnalyzer:

    def __init__(
        self,
        llm_client
    ):

        self.llm = llm_client

    def analyze(
        self,
        text
    ):

        prompt = (
            DISRUPTION_RISK_PROMPT
            .format(
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

                "efficient_ai_risk": 0,

                "compute_reduction_risk": 0,

                "low_power_ai_risk": 0,

                "open_source_disruption": 0,

                "alternative_paradigm_risk": 0,

                "summary":
                    "LLM parsing failed"
            }