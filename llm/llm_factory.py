import json

from llm.gemini_client import (
    GeminiClient
)

from llm.claude_client import (
    ClaudeClient
)


class LLMFactory:

    @staticmethod
    def create_llm():

        with open(

            "configs/llm_config.json",

            "r",

            encoding="utf-8"

        ) as f:

            config = json.load(f)

        provider = config[
            "active_provider"
        ]

        provider_config = config[
            "providers"
        ][provider]

        
        api_key = provider_config[
            "api_key"
        ]

        base_url = provider_config.get(
            "base_url"
        )

        if provider == "gemini":

            return GeminiClient(
                api_key
            )

        elif provider == "claude":
            
            return ClaudeClient(

                api_key,

                base_url
            )

        else:

            raise ValueError(
                f"Unsupported LLM "
                f"provider: {provider}"
            )