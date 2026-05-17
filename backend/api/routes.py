from fastapi import APIRouter

import asyncio
import json
from datetime import datetime

from sse_starlette.sse import EventSourceResponse

from backend.orchestration.billing_workflow import (
    graph
)

from backend.agents.billing_agent.agent import (
    investigate
)

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "running"
    }


@router.get("/billing/{customer_id}")
def investigate_bill(customer_id: str):

    result = investigate(customer_id)

    return {
        "customer_id": customer_id,
        "investigation": result
    }


@router.get("/workflow/{customer_id}")

def run_workflow(customer_id: str):

    result = graph.invoke({

        "customer_id": customer_id,

        "timeline": []

    })

    return result



@router.get("/workflow-stream/{customer_id}")

async def workflow_stream(customer_id: str):

    async def event_generator():

        events = [

            {
                "agent": "Billing Agent",

                "message":
                    "Retrieved billing history",

                "time":
                    datetime.now().strftime("%H:%M:%S"),

                "status":
                    "COMPLETE"
            },

            {
                "agent": "VEE Agent",

                "message":
                    "Validated interval quality",

                "time":
                    datetime.now().strftime("%H:%M:%S"),

                "status":
                    "COMPLETE"
            },

            {
                "agent": "Forecast Agent",

                "message":
                    "Compared seasonal forecast",

                "time":
                    datetime.now().strftime("%H:%M:%S"),

                "status":
                    "COMPLETE"
            },

            {
                "agent": "Outage Agent",

                "message":
                    "Checked outage correlation",

                "time":
                    datetime.now().strftime("%H:%M:%S"),

                "status":
                    "COMPLETE"
            },

            {
                "agent": "Decision Agent",

                "message":
                    "Generated final assessment",

                "time":
                    datetime.now().strftime("%H:%M:%S"),

                "status":
                    "COMPLETE"
            }
        ]

        for event in events:

            await asyncio.sleep(1)

            yield {

                "event": "message",

                "data": json.dumps(event)
            }

    return EventSourceResponse(
        event_generator()
    )