"""
graph/nodes.py

LangGraph Nodes
"""

from agents.parser_agent import (
    ParserAgent
)

from agents.analytics_agent import (
    AnalyticsAgent
)

from agents.search_agent import (
    SearchAgent
)

from agents.recommendation_agent import (
    RecommendationAgent
)

from agents.college_research_agent import (
    CollegeResearchAgent
)

from agents.chatbot_agent import (
    ChatbotAgent
)

from graph.state import (
    CollegeState
)


# =====================================================
# AGENTS
# =====================================================

parser_agent = ParserAgent()

analytics_agent = AnalyticsAgent()

search_agent = SearchAgent()

recommendation_agent = (
    RecommendationAgent()
)

research_agent = (
    CollegeResearchAgent()
)

chatbot_agent = (
    ChatbotAgent()
)


# =====================================================
# PARSER NODE
# =====================================================

def parser_node(
    state: CollegeState
):

    result = parser_agent.run(
        state["query"]
    )

    state["parsed_data"] = result

    return state


# =====================================================
# ANALYTICS NODE
# =====================================================

def analytics_node(
    state: CollegeState
):

    result = analytics_agent.run(
        state["query"]
    )

    state["analytics_result"] = (
        result
    )

    return state


# =====================================================
# SEARCH NODE
# =====================================================

def search_node(
    state: CollegeState
):

    result = search_agent.run(
        state["query"]
    )

    state["search_result"] = (
        result
    )

    return state


# =====================================================
# RECOMMENDATION NODE
# =====================================================

def recommendation_node(
    state: CollegeState
):

    result = (
        recommendation_agent.run(
            state["query"]
        )
    )

    state[
        "recommendation_result"
    ] = result

    return state


# =====================================================
# RESEARCH NODE
# =====================================================

def research_node(
    state: CollegeState
):

    result = (
        research_agent.run(
            state["query"]
        )
    )

    state["research_result"] = (
        result
    )

    return state


# =====================================================
# CHATBOT NODE
# =====================================================

def chatbot_node(
    state: CollegeState
):

    result = chatbot_agent.run(
        state["query"]
    )

    state[
        "chatbot_response"
    ] = result

    return state


# =====================================================
# ROUTER
# =====================================================

def router_node(
    state: CollegeState
):

    query = (
        state["query"]
        .lower()
    )

    if "analytics" in query:

        return "analytics"

    elif "recommend" in query:

        return "recommendation"

    elif "college" in query:

        return "research"

    elif "search" in query:

        return "search"

    else:

        return "chatbot"
