import json
from llm.prompts.prompts import (
    MOAT_ANALYSIS_PROMPT
)

class MoatLLMAnalyzer:

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
            MOAT_ANALYSIS_PROMPT
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

            parsed = json.loads(
                response
            )

            return parsed

        except Exception:

            return {

                "ecosystem_lockin": 0,
                "switching_costs": 0,
                "strategic_importance": 0,
                "supply_chain_bottleneck": 0,
                "proprietary_technology": 0,
                "infrastructure_criticality": 0,
                "summary": "LLM parsing failed"
            }