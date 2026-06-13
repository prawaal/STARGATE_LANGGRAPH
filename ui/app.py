import streamlit as st

import subprocess
import json
import pandas as pd
import os
import sys
import time


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(

    page_title=
        "AI Factory Intelligence",

    layout="wide"
)


# -----------------------------------
# TITLE
# -----------------------------------

st.title(
    "AI Factory Intelligence"
)


# -----------------------------------
# STATUS PLACEHOLDERS
# -----------------------------------

status_placeholder = st.empty()

progress_placeholder = st.empty()


# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.header(
        "LLM Settings"
    )


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


    # -----------------------------------
    # STORE ENV
    # -----------------------------------

    if api_key:

        os.environ[
            "LLM_PROVIDER"
        ] = provider


        os.environ[
            "LLM_API_KEY"
        ] = api_key


        st.success(
            "LLM configured"
        )


# -----------------------------------
# BASE DIRECTORY
# -----------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# -----------------------------------
# IMAGE
# -----------------------------------

image_path = os.path.join(

    BASE_DIR,

    "ui",

    "agent_flow.png"
)


st.image(
    image_path,
    width="stretch"
)


# -----------------------------------
# AGENTS
# -----------------------------------

agents = [

    "Research",

    "Discovery",

    "Ingestion",

    "Scoring",

    "Ranking"
]


# -----------------------------------
# SELECT START POINT
# -----------------------------------

selected_agent = st.radio(

    "Select workflow starting point",

    agents,

    horizontal=True
)


# -----------------------------------
# RUN FROM
# -----------------------------------

run_from = (
    selected_agent.lower()
)


# -----------------------------------
# RUN BUTTON
# -----------------------------------

st.markdown("")


if st.button(
    "Trigger Workflow"
):

    st.info(

        f"Running workflow "
        f"from {selected_agent}"
    )


    # -----------------------------------
    # STATUS FILE
    # -----------------------------------

    status_path = os.path.join(

        BASE_DIR,

        "outputs",

        "runtime_status.json"
    )


    # -----------------------------------
    # START PROCESS
    # -----------------------------------

    process = subprocess.Popen([

        sys.executable,

        "-m",

        "graph.stargate_graph",

        run_from
    ])


    # -----------------------------------
    # POLL STATUS
    # -----------------------------------

    while process.poll() is None:

        if os.path.exists(
            status_path
        ):

            try:

                with open(

                    status_path,

                    "r",

                    encoding="utf-8"

                ) as f:

                    runtime_status = json.load(f)


                # -----------------------------------
                # STATUS TEXT
                # -----------------------------------

                status_placeholder.info(

                    runtime_status[
                        "agent"
                    ]
                )


                # -----------------------------------
                # PROGRESS BAR
                # -----------------------------------

                progress_placeholder.progress(

                    runtime_status[
                        "progress"
                    ]
                )

            except Exception:

                pass


        time.sleep(1)


    # -----------------------------------
    # COMPLETE
    # -----------------------------------

    status_placeholder.success(
        "Workflow Complete"
    )


    progress_placeholder.progress(
        100
    )


    # -----------------------------------
    # LOAD RESULTS
    # -----------------------------------

    rankings_path = os.path.join(

        BASE_DIR,

        "outputs",

        "final_ai_factory_rankings.json"
    )


    if os.path.exists(
        rankings_path
    ):

        with open(

            rankings_path,

            "r",

            encoding="utf-8"

        ) as f:

            rankings = json.load(f)


        # -----------------------------------
        # TOP 20 TABLE
        # -----------------------------------

        st.subheader(
            "Top 20 AI Factory Companies"
        )


        df = pd.DataFrame(
            rankings[:20]
        )


        # -----------------------------------
        # START INDEX FROM 1
        # -----------------------------------

        df.index = (
            df.index + 1
        )


        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.error(
            "Ranking file not found"
        )
