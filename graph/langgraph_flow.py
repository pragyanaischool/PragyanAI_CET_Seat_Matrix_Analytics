"""
graph/langgraph_flow.py

Main LangGraph Workflow
"""

from langgraph.graph import (
    StateGraph,
    END
)

from graph.state import (
    CollegeState
)

from graph.nodes import (

    parser_node,

    analytics_node,

    search_node,

    recommendation_node,

    research_node,

    chatbot_node,

    router_node
)


class CollegeLangGraph:

    def __init__(self):

        self.workflow = (
            StateGraph(
                CollegeState
            )
        )

        self.build_graph()

    def build_graph(
        self
    ):

        # ====================================
        # NODES
        # ====================================

        self.workflow.add_node(
            "parser",
            parser_node
        )

        self.workflow.add_node(
            "analytics",
            analytics_node
        )

        self.workflow.add_node(
            "search",
            search_node
        )

        self.workflow.add_node(
            "recommendation",
            recommendation_node
        )

        self.workflow.add_node(
            "research",
            research_node
        )

        self.workflow.add_node(
            "chatbot",
            chatbot_node
        )

        # ====================================
        # ENTRY
        # ====================================

        self.workflow.set_entry_point(
            "parser"
        )

        # ====================================
        # ROUTING
        # ====================================

        self.workflow.add_conditional_edges(

            "parser",

            router_node,

            {

                "analytics":
                    "analytics",

                "search":
                    "search",

                "recommendation":
                    "recommendation",

                "research":
                    "research",

                "chatbot":
                    "chatbot"
            }
        )

        # ====================================
        # END STATES
        # ====================================

        self.workflow.add_edge(
            "analytics",
            END
        )

        self.workflow.add_edge(
            "search",
            END
        )

        self.workflow.add_edge(
            "recommendation",
            END
        )

        self.workflow.add_edge(
            "research",
            END
        )

        self.workflow.add_edge(
            "chatbot",
            END
        )

        self.graph = (
            self.workflow.compile()
        )

    def invoke(
        self,
        query
    ):

        return self.graph.invoke(

            {
                "query": query
            }

        )


college_graph = (
    CollegeLangGraph()
)
