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

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.ai-header {
    background: linear-gradient(
        90deg,
        #0f172a 0%,
        #1e3a8a 35%,
        #2563eb 70%,
        #06b6d4 100%
    );
    padding: 1.2rem 2rem;
    border-radius: 12px;
    margin-bottom: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.ai-title {
    color: white;
    font-size: 2rem;
    font-weight: 800;
    margin: 0;
}

.ai-subtitle {
    color: #dbeafe;
    font-size: 1rem;
    margin-top: 0.2rem;
}
</style>

<div class="ai-header">
    <div class="ai-title">🏭 AI Factory Intelligence</div>
    <div class="ai-subtitle">
        Discovering Public Companies positioned to achieve equity growth driven by global build-out of AI Factories.
    </div>
</div>
""", unsafe_allow_html=True)

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
