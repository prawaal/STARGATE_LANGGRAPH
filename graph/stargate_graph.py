from langgraph.graph import (
    StateGraph,
    END
)

from state.stargate_state import (
    StargateState
)

from agents.research_agent import (
    ResearchAgent
)

from agents.discovery_agent import (
    DiscoveryAgent
)

from agents.ingestion_agent import (
    IngestionAgent
)

from agents.scoring_agent import (
    ScoringAgent
)

from agents.ranking_agent import (
    RankingAgent
)

from agents.insight_agent import (
    InsightAgent
)


# -----------------------------------
# INIT AGENTS
# -----------------------------------

research_agent = (
    ResearchAgent()
)

discovery_agent = (
    DiscoveryAgent()
)

ingestion_agent = (
    IngestionAgent()
)

scoring_agent = (
    ScoringAgent()
)

ranking_agent = (
    RankingAgent()
)

insight_agent = (
    InsightAgent()
)

def entry_router(state):

    run_from = state.get(
        "run_from",
        "research"
    )

    return run_from
# -----------------------------------
# BUILD GRAPH
# -----------------------------------

graph = StateGraph(
    StargateState
)


graph.add_node(

    "research",

    research_agent.run
)

graph.add_node(

    "discovery",

    discovery_agent.run
)

graph.add_node(

    "ingestion",

    ingestion_agent.run
)

graph.add_node(

    "scoring",

    scoring_agent.run
)

graph.add_node(

    "ranking",

    ranking_agent.run
)

graph.add_node(

    "insights",

    insight_agent.run
)


# -----------------------------------
# FLOW
# -----------------------------------

graph.set_conditional_entry_point(
    entry_router
)

graph.add_edge(
    "research",
    "discovery"
)

graph.add_edge(
    "discovery",
    "ingestion"
)

graph.add_edge(
    "ingestion",
    "scoring"
)

graph.add_edge(
    "scoring",
    "ranking"
)

graph.add_edge(
    "ranking",
    "insights"
)

graph.add_edge(
    "insights",
    END
)


# -----------------------------------
# COMPILE
# -----------------------------------

app = graph.compile()


# -----------------------------------
# RUN
# -----------------------------------

initial_state = {

    "run_from": "scoring",

    "final_rankings_path": ""
}


app.invoke(
    initial_state
)