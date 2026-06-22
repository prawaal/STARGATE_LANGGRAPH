import streamlit as st
import os


def render_llm_config():

    with st.expander(

        "⚙️ LLM Configuration",

        expanded=False
    ):

        # -----------------------------------
        # MODEL OPTIONS
        # -----------------------------------

        MODEL_OPTIONS = {

            "gemini": [

                "gemini-2.5-flash",

                "gemini-2.5-pro"
            ],

            "claude": [

                "claude-sonnet-4",

                "claude-opus-4"
            ],

            "ollama": [

                "llama3",

                "llama3.1",

                "mistral",

                "deepseek-r1"
            ],

            "nollm": [

                "none"
            ]
        }


        provider = st.selectbox(

            "Provider",

            [

                "gemini",

                "claude",

                "ollama",

                "nollm"
            ]
        )


        model_name = st.selectbox(

            "Model",

            MODEL_OPTIONS[
                provider
            ]
        )

        if provider in [

            "ollama",

            "nollm"
        ]:

            st.text_input(

                "API Key",

                value="Not Required",

                disabled=True
            )

            api_key = ""

        else:

            api_key = st.text_input(

                "API Key",

                type="password"
            )

        if st.button(
            "Apply Configuration"
        ):

            os.environ[
                "LLM_PROVIDER"
            ] = provider

            os.environ[
                "LLM_MODEL"
            ] = model_name

            os.environ[
                "LLM_API_KEY"
            ] = api_key

            st.success(

                f"{provider} configured"
            )
