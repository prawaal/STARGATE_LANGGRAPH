import json
import os

from llm.gemini_client import (
    GeminiClient
)

from llm.claude_client import (
    ClaudeClient
)


class LLMFactory:

    @staticmethod
    def create_llm():

        # -----------------------------------
        # LOAD CONFIG
        # -----------------------------------

        config = {}

        config_path = (
            "configs/llm_config.json"
        )


        if os.path.exists(
            config_path
        ):

            with open(

                config_path,

                "r",

                encoding="utf-8"

            ) as f:

                config = json.load(f)


        # -----------------------------------
        # CONFIG VALUES
        # -----------------------------------

        active_provider = config.get(
            "active_provider",
            "gemini"
        )


        provider_config = config.get(
            "providers",
            {}
        ).get(
            active_provider,
            {}
        )


        # -----------------------------------
        # ENV OVERRIDES
        # -----------------------------------

        provider = os.getenv(

            "LLM_PROVIDER",

            active_provider
        )


        api_key = os.getenv(

            "LLM_API_KEY",

            provider_config.get(
                "api_key",
                ""
            )
        )


        base_url = os.getenv(

            "LLM_BASE_URL",

            provider_config.get(
                "base_url",
                None
            )
        )


        # -----------------------------------
        # CREATE CLIENT
        # -----------------------------------

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
