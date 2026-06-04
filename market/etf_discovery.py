import json

from ontology.prompts import (
    ETF_DISCOVERY_PROMPT
)


class ETFDiscovery:

    def __init__(self, llm_client):

        self.llm_client = llm_client

    def discover_etfs(
        self,
        category,
        subcategories
    ):

        subcategory_text = ", ".join(

            [
                s["name"]
                for s in subcategories
            ]
        )

        prompt = (
            ETF_DISCOVERY_PROMPT
            .replace("{category}", category)
            .replace(
                "{subcategories}",
                subcategory_text
            )
        )

        response = self.llm_client.generate(
            prompt
        )

        response = response.strip()

        if response.startswith("```json"):

            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(response)