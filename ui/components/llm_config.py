import streamlit as st
import os


def render_llm_config():

    with st.expander(

        "⚙️ LLM Configuration",

        expanded=False
    ):

        provider = st.selectbox(

            "Provider",

            [

                "gemini",

                "claude",

                "ollama",

                "nollm"
            ]
        )


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
                "LLM_API_KEY"
            ] = api_key


            st.success(

                f"{provider} configured"
            )
