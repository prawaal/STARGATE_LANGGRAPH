import streamlit as st
import json
import os
import plotly.graph_objects as go



# -----------------------------------
# COLOR LOGIC
# -----------------------------------

def get_tile_color(score):

    if score >= 0.75:

        return "#2E8B57"      # Green

    elif score >= 0.50:

        return "#FFD700"      # Yellow

    elif score >= 0.25:

        return "#FF8C00"      # Orange

    return "#CD5C5C"          # Red


# -----------------------------------
# COMPANY DIALOG
# -----------------------------------

@st.dialog("Company Intelligence")
def show_company_dialog(company):

    st.subheader(
        company["company_name"]
    )

    st.caption(
        company["symbol"]
    )

    st.write(
        f"Category: {company['category']}"
    )


    # -----------------------------
    # RADAR CHART
    # -----------------------------

    categories = [

        "Moat",

        "Financial",

        "AI Exposure",

        "Growth"
    ]


    values = [

        company.get(
            "moat_score",
            0
        ) * 100,

        company.get(
            "financial_score",
            0
        ) * 100,

        company.get(
            "ai_exposure_score",
            0
        ) * 100,

        company.get(
            "forward_growth_score",
            0
        ) * 100
    ]


    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            name=company[
                "symbol"
            ]
        )
    )


    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0, 100]
            )
        ),

        showlegend=False,

        height=400
    )


    st.plotly_chart(

        fig,

        width="stretch"
    )
   

    st.divider()

    # -----------------------------
    # SCORE SUMMARY
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Moat",

            round(
                company.get(
                    "moat_score",
                    0
                ) * 100,
                1
            )
        )

        st.metric(

            "Financial",

            round(
                company.get(
                    "financial_score",
                    0
                ) * 100,
                1
            )
        )

    with col2:

        st.metric(

            "AI Exposure",

            round(
                company.get(
                    "ai_exposure_score",
                    0
                ) * 100,
                1
            )
        )

        st.metric(

            "Forward Growth",

            round(
                company.get(
                    "forward_growth_score",
                    0
                ) * 100,
                1
            )
        )

    with col3:

        st.metric(

            "Final Score",

            round(
                company.get(
                    "final_score",
                    0
                ) * 100,
                1
            )
        )

        st.metric(

            "Disruption",

            round(
                company.get(
                    "disruption_multiplier",
                    0
                ),
                2
            )
        )

    st.divider()

    # -----------------------------
    # EXTRA DETAILS
    # -----------------------------

    st.write(

        f"Structural Advantage: "
        f"{round(company.get('structural_advantage',0)*100,1)}"
    )

    st.write(

        f"Core Growth Score: "
        f"{round(company.get('core_growth_score',0)*100,1)}"
    )

    st.write(

        f"Effective Disruption: "
        f"{round(company.get('effective_disruption',0)*100,1)}"
    )

    st.divider()

    st.json(
        company,
        expanded=False
    )


# -----------------------------------
# COMPANY TILE
# -----------------------------------


def render_company_tile(company):

    score = company.get(
        "normalized_score",
        0
    )

    score_pct = round(
        score * 100,
        1
    )

    color = get_tile_color(
        score
    )

    with st.container():

        st.markdown(
            f"""
            <div style="
                background-color:{color};
                padding:12px;
                border-radius:10px;
                text-align:center;
                color:white;
                margin-bottom:0px;
            ">
                <b>{company['symbol']}</b><br>
                Score {score_pct}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "View Details",
            key=f"detail_{company['symbol']}_{company['category']}",
            use_container_width=True
        ):
            show_company_dialog(
                company
            )






# -----------------------------------
# MAIN TAB
# -----------------------------------

def render_landscape_tab():

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

    categories = {}

    for company in rankings:

        category = company.get(

            "category",

            "Uncategorized"
        )

        #print(category)

        categories.setdefault(

            category,

            []

        ).append(
            company
        )

    st.subheader(
        "AI Factory Landscape"
    )

    st.caption(
        "Companies grouped by AI Factory value chain category"
    )


    # -----------------------------
    # CATEGORY LAYOUT
    # -----------------------------

    DISPLAY_ORDER = [

        "Compute Infrastructure",

        "Power Infrastructure",

        "Cooling Infrastructure",

        "Network Infrastructure",

        "Physical Infrastructure",

        "Semiconductor Supply Chain",

        "AI Operations & Services"
    ]


    DISPLAY_NAMES = {

        "Compute Infrastructure": "Compute",

        "Power Infrastructure": "Power",

        "Cooling Infrastructure": "Cooling",

        "Network Infrastructure": "Network",

        "Physical Infrastructure": "Physical",

        "Semiconductor Supply Chain": "Supply Chain",

        "AI Operations & Services": "AI Services"
    }


    available_categories = [

        category

        for category in DISPLAY_ORDER

        if category in categories
    ]


    category_cols = st.columns(
        len(available_categories)
    )


    for idx, category in enumerate(
        available_categories
    ):

        with category_cols[idx]:

            st.markdown(
                f"""
                <div style="
                    background-color:#1E293B;
                    color:white;
                    padding:10px;
                    border-radius:8px;
                    text-align:center;
                    font-weight:bold;
                    margin-bottom:10px;
                ">
                    {DISPLAY_NAMES.get(category, category)}
                    <br>
                    {len(categories[category])} Companies
                </div>
                """,
                unsafe_allow_html=True
            )    

            companies = categories[
                category
            ]

            for i in range(

                0,

                len(companies),

                2
            ):

                tile_cols = st.columns(2)

                # -----------------
                # FIRST TILE
                # -----------------

                with tile_cols[0]:

                    render_company_tile(

                        companies[i]
                    )

                # -----------------
                # SECOND TILE
                # -----------------

                if i + 1 < len(
                    companies
                ):

                    with tile_cols[1]:

                        render_company_tile(

                            companies[
                                i + 1
                            ]
                        )
