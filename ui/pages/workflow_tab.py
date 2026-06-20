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
    # DEFAULT AGENT
    # -----------------------------------

    if "run_from" not in st.session_state:

        st.session_state[
            "run_from"
        ] = "scoring"

    # -----------------------------------
    # AGENTS
    # -----------------------------------

    
    st.subheader(
        "Select Starting Agent"
    )


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        if st.button(

            "📊 Research",

            key="research_tile",

            use_container_width=True
        ):

            st.session_state[
                "run_from"
            ] = "research"

            st.rerun()     

    with col2:

        if st.button(

            "📊 Discovery",

            key="discovery_tile",

            use_container_width=True
        ):

            st.session_state[
                "run_from"
            ] = "discovery"

            st.rerun()          

    with col3:        

        if st.button(

            "📥 Ingestion",

            key="ingestion_tile",

            use_container_width=True
        ):

            st.session_state[
                "run_from"
            ] = "ingestion"

            st.rerun()        

    with col4:

        if st.button(

            "📊 Scoring",

            key="scoring_tile",

            use_container_width=True
        ):

            st.session_state[
                "run_from"
            ] = "scoring"

            st.rerun()

    with col5:

        if st.button(

            "🏆 Ranking",

            key="ranking_tile",

            use_container_width=True
        ):

            st.session_state[
                "run_from"
            ] = "ranking"

            st.rerun()



    run_from = st.session_state[
        "run_from"
    ]


    st.info(

        f"Selected Agent: "

        f"{st.session_state['run_from'].title()}"
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
    # TRIGGER WORKFLOW
    # -----------------------------------

    if st.button(
        "🚀 Trigger Workflow",
        use_container_width=True
    ):

        status_path = os.path.join(

            BASE_DIR,

            "outputs",

            "runtime_status.json"
        )

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

        rankings_path = os.path.join( BASE_DIR, "outputs", "final_ai_factory_rankings.json" )

        if os.path.exists( rankings_path ): 

            with open( rankings_path, "r", encoding="utf-8" ) as f: 

                rankings = json.load( f )
        
        st.markdown("---")

        st.subheader(
            "🏆 AI Factory Leaders"
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


        rankings = list(
            symbol_map.values()
        )


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
                "normalized_score"
            ],

            reverse=True
        )


        gold = []
        silver = []
        bronze = []

        for company in rankings[:20]:

            score = company[
                "normalized_score"
            ]

            if score >= 0.75:

                gold.append(
                    company
                )

            elif score >= 0.50:

                silver.append(
                    company
                )

            else:

                bronze.append(
                    company
                )


        gold_col, silver_col, bronze_col = st.columns(3)


        with gold_col:

            st.markdown(
                "## 🥇 Gold"
            )

            for company in gold:

                st.markdown(

                    f"""
                    <div style="
                        background-color:#FFD700;
                        color:black;
                        padding:10px;
                        border-radius:10px;
                        margin-bottom:8px;
                    ">
                        <b>{company['symbol']}</b><br>
                        {company['company_name']}<br>
                        Score: {round(company['normalized_score']*100,1)}
                    </div>
                    """,

                    unsafe_allow_html=True
                )


        with silver_col:

            st.markdown(
                "## 🥈 Silver"
            )

            for company in silver:

                st.markdown(

                    f"""
                    <div style="
                        background-color:#C0C0C0;
                        color:black;
                        padding:10px;
                        border-radius:10px;
                        margin-bottom:8px;
                    ">
                        <b>{company['symbol']}</b><br>
                        {company['company_name']}<br>
                        Score: {round(company['normalized_score']*100,1)}
                    </div>
                    """,

                    unsafe_allow_html=True
                )


        with bronze_col:

            st.markdown(
                "## 🥉 Bronze"
            )

            for company in bronze:

                st.markdown(

                    f"""
                    <div style="
                        background-color:#CD7F32;
                        color:white;
                        padding:10px;
                        border-radius:10px;
                        margin-bottom:8px;
                    ">
                        <b>{company['symbol']}</b><br>
                        {company['company_name']}<br>
                        Score: {round(company['normalized_score']*100,1)}
                    </div>
                    """,

                    unsafe_allow_html=True
                )
