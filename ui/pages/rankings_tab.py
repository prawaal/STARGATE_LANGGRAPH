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


    df = pd.DataFrame(
        rankings
    )


    if "final_score" in df.columns:

        df[
            "final_score"
        ] = (

            df[
                "final_score"
            ] * 100

        ).round(2)


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
