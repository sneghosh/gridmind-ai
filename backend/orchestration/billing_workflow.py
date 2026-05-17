from typing import TypedDict
from typing import Annotated

from operator import add

from langgraph.graph import (
    StateGraph,
    END,
    START
)

import time

# -----------------------------------
# STATE
# -----------------------------------

class BillingState(TypedDict):

    customer_id: str

    billing_analysis: str

    vee_validation: str

    forecast_analysis: str

    outage_analysis: str

    final_decision: str

    timeline: Annotated[list, add]


# -----------------------------------
# AGENTS
# -----------------------------------

def billing_agent(state):

    time.sleep(1)

    print("Running Billing Agent")

    return {

        "billing_analysis":
            "Detected abnormal consumption spike.",

        "timeline": [

            {
                "agent": "Billing Agent",

                "message":
                    "Retrieved billing history and analyzed usage.",

                "status": "COMPLETE"
            }
        ]
    }


def vee_agent(state):

    time.sleep(1)

    print("Running VEE Agent")

    return {

        "vee_validation":
            "No interval estimation anomalies detected.",

        "timeline": [

            {
                "agent": "VEE Agent",

                "message":
                    "Validated interval quality and estimation.",

                "status": "COMPLETE"
            }
        ]
    }


def forecast_agent(state):

    time.sleep(1)

    print("Running Forecast Agent")

    return {

        "forecast_analysis":
            "Consumption exceeds seasonal forecast.",

        "timeline": [

            {
                "agent": "Forecast Agent",

                "message":
                    "Compared against seasonal forecast baseline.",

                "status": "COMPLETE"
            }
        ]
    }



def outage_agent(state):

    time.sleep(1)

    print("Running Outage Agent")

    return {

        "outage_analysis":
            "No outage correlation identified.",

        "timeline": [

            {
                "agent": "Outage Agent",

                "message":
                    "Checked outage correlation patterns.",

                "status": "COMPLETE"
            }
        ]
    }




def decision_agent(state):

    time.sleep(1)

    print("Running Decision Agent")

    return {

        "final_decision":
            "Bill appears valid. High confidence assessment.",

        "timeline": [

            {
                "agent": "Decision Agent",

                "message":
                    "Generated final billing assessment.",

                "status": "COMPLETE"
            }
        ]
    }


# -----------------------------------
# GRAPH
# -----------------------------------

workflow = StateGraph(BillingState)

workflow.add_node(
    "billing_agent",
    billing_agent
)

workflow.add_node(
    "vee_agent",
    vee_agent
)

workflow.add_node(
    "forecast_agent",
    forecast_agent
)

workflow.add_node(
    "outage_agent",
    outage_agent
)

workflow.add_node(
    "decision_agent",
    decision_agent
)

# FLOW

# workflow.set_entry_point(
#     "billing_agent"
# )

# workflow.add_edge(
#     "billing_agent",
#     "vee_agent"
# )

# workflow.add_edge(
#     "vee_agent",
#     "forecast_agent"
# )

# workflow.add_edge(
#     "forecast_agent",
#     "outage_agent"
# )

# workflow.add_edge(
#     "outage_agent",
#     "decision_agent"
# )

# workflow.add_edge(
#     "decision_agent",
#     END
# )


# -----------------------------------
# PARALLEL FLOW
# -----------------------------------

workflow.add_edge(
    START,
    "billing_agent"
)

# Billing agent fans out

workflow.add_edge(
    "billing_agent",
    "vee_agent"
)

workflow.add_edge(
    "billing_agent",
    "forecast_agent"
)

workflow.add_edge(
    "billing_agent",
    "outage_agent"
)

# All converge into decision

workflow.add_edge(
    "vee_agent",
    "decision_agent"
)

workflow.add_edge(
    "forecast_agent",
    "decision_agent"
)

workflow.add_edge(
    "outage_agent",
    "decision_agent"
)

workflow.add_edge(
    "decision_agent",
    END
)

graph = workflow.compile()