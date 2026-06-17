import streamlit as st

from pages.workflow_tab import (
    render_workflow_tab
)

from pages.landscape_tab import (
    render_landscape_tab
)

from pages.rankings_tab import (
    render_rankings_tab
)

from components.llm_config import (
    render_llm_config
)


st.set_page_config(

    page_title=
        "AI Factory Intelligence",

    layout="wide"
)


st.title(
    "AI Factory Intelligence"
)


render_llm_config()


tab1, tab2, tab3 = st.tabs([

    "Workflow",

    "AI Factory Landscape",

    "Rankings"
])


with tab1:

    render_workflow_tab()


with tab2:

    render_landscape_tab()


with tab3:

    render_rankings_tab()
