import streamlit as st

import subprocess
import json
import pandas as pd
import os
import sys
import time


def render_workflow_tab():

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    # -----------------------------------
    # STATUS PLACEHOLDERS
    # -----------------------------------

    status_placeholder = st.empty()

    progress_placeholder = st.empty()

    # -----------------------------------
    # IMAGE
    # -----------------------------------

    image_path = os.path.join(

        BASE_DIR,

        "ui",

        "agent_flow.png"
    )

    if os.path.exists(
        image_path
    ):

        st.image(
            image_path,
            width="stretch"
        )

    # -----------------------------------
    # AGENTS
    # -----------------------------------

    st.caption(
        "Research, Discovery and Ingestion "
        "have already been completed."
    )

    agents = [
        "Research", 
        "Discovery",
        "Ingestion",
        "Scoring",
        "Ranking"
    ]

    selected_agent = st.radio(

        "Select workflow starting point",

        agents,

        horizontal=True
    )

    run_from = (
        selected_agent.lower()
    )

    st.markdown("")

    # -----------------------------------
    # RUN BUTTON
    # -----------------------------------

    if st.button(
        "Trigger Workflow",
        key="workflow_button"
    ):

        st.info(

            f"Running workflow "
            f"from {selected_agent}"
        )

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

                        runtime_status = json.load(
                            f
                        )

                    status_placeholder.info(

                        runtime_status.get(

                            "agent",

                            "Running..."
                        )
                    )

                    progress_placeholder.progress(

                        runtime_status.get(

                            "progress",

                            0
                        )
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
    # SHOW CURRENT RANKINGS
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

            rankings = json.load(
                f
            )

        st.markdown("---")

        st.subheader(
            "Current Top 20 Rankings"
        )

        symbol_map = {}

        for company in rankings:

            symbol = company["symbol"]

            if symbol not in symbol_map:

                symbol_map[symbol] = company.copy()

                symbol_map[symbol]["all_categories"] = [
                    company["category"]
                ]

            else:

                symbol_map[symbol][
                    "all_categories"
                ].append(
                    company["category"]
                )

                if (
                    company["final_score"]
                    >
                    symbol_map[symbol][
                        "final_score"
                    ]
                ):

                    existing_categories = (
                        symbol_map[symbol][
                            "all_categories"
                        ]
                    )

                    symbol_map[symbol] = (
                        company.copy()
                    )

                    symbol_map[symbol][
                        "all_categories"
                    ] = (
                        existing_categories
                    )
                    
        rankings = list(symbol_map.values())
        for company in rankings:

            company["category"] = ", ".join(

            sorted(

                set(

                    company[
                        "all_categories"
                    ]

                )

            )

        )

        rankings.sort(

            key=lambda x: x[
                "final_score"
            ],

            reverse=True
        )
        
        df = pd.DataFrame(rankings)

        df = df[

            [

                "symbol",

                "company_name",

                "category",

                "final_score"

            ]

        ]

        df["final_score"] = (

            df["final_score"]

            * 100

        ).round(2)

        df.index = (
            df.index + 1
        )

        st.dataframe(

            df.head(20),

            width="stretch"
        )
