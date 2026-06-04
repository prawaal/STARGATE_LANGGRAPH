import json

from llm.prompts import (
    ONTOLOGY_DECOMPOSITION_PROMPT
)


class OntologyDecomposer:

    def __init__(self, llm_client):

        self.llm_client = llm_client

    def decompose(self, category):

        prompt = (
            ONTOLOGY_DECOMPOSITION_PROMPT
            .replace("{category}", category)
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