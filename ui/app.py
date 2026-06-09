import streamlit as st

import subprocess
import json
import pandas as pd
import os
import sys

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(

    page_title=
        "STARGATE AI Factory",

    layout="wide"
)


# -----------------------------------
# TITLE
# -----------------------------------

st.title(
    "STARGATE AI Factory Intelligence"
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
    # RUN LANGGRAPH
    # -----------------------------------

    subprocess.run([

        sys.executable,

        "-m",

        "graph.stargate_graph",

        run_from
    ])


    st.success(
        "Workflow Complete"
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

        df.index = df.index + 1


        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.error(
            "Ranking file not found"
        )
