import streamlit as st
import pandas as pd
import json
import os


def render_rankings_tab():

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    rankings_path = os.path.join(

        BASE_DIR,

        "outputs",

        "final_ai_factory_rankings.json"
    )

    if not os.path.exists(
        rankings_path
    ):

        st.warning(
            "No rankings available"
        )

        return

    with open(

        rankings_path,

        "r",

        encoding="utf-8"

    ) as f:

        rankings = json.load(f)

    # -----------------------------------
    # DEDUPLICATE COMPANIES
    # -----------------------------------

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
                ] = existing_categories

    rankings = list(
        symbol_map.values()
    )

    # -----------------------------------
    # MERGE CATEGORY LIST
    # -----------------------------------

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

    # -----------------------------------
    # CATEGORY FILTER
    # -----------------------------------

    category_options = sorted(

        list(

            set(

                category

                for company in rankings

                for category in company[
                    "all_categories"
                ]

            )

        )

    )

    selected_categories = st.multiselect(

        "Filter Categories",

        category_options
    )

    if selected_categories:

        rankings = [

            company

            for company in rankings

            if any(

                category in company[
                    "all_categories"
                ]

                for category in selected_categories

            )

        ]

    # -----------------------------------
    # SORT
    # -----------------------------------

    rankings.sort(

        key=lambda x:

        x.get(
            "normalized_score",
            0
        ),

        reverse=True
    )

    # -----------------------------------
    # DATAFRAME
    # -----------------------------------

    df = pd.DataFrame(
        rankings
    )

    display_columns = [

        "rank",

        "symbol",

        "company_name",

        "category",

        "normalized_score"
    ]

    available_columns = [

        col

        for col in display_columns

        if col in df.columns
    ]

    df = df[
        available_columns
    ]

    if "normalized_score" in df.columns:

        df.rename(

            columns={

                "normalized_score":
                "AI Factory Score"

            },

            inplace=True
        )

    st.subheader(
        "AI Factory Rankings"
    )

    df.index = (
        df.index + 1
    )

    st.dataframe(

        df,

        width="stretch"
    )
