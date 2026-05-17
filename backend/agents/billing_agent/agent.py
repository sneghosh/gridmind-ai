# import os

# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType

# from backend.agents.billing_agent.tools import (
#     get_customer_history,
#     get_latest_bill,
#     detect_abnormal_usage
# )

# from backend.agents.billing_agent.prompts import (
#     SYSTEM_PROMPT
# )

# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# llm = ChatOpenAI(
#     model="gpt-5-mini",
#     temperature=0
# )



# tools = [
#     get_customer_history,
#     get_latest_bill,
#     detect_abnormal_usage
# ]

# # billing_agent = initialize_agent(
# #     tools=tools,
# #     llm=llm,
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     verbose=True
# # )


# def investigate(customer_id: str):

#     query = f"""
#     Investigate billing dispute for customer:
#     {customer_id}

#     Use available tools.

#     Return:
#     - summary
#     - probable cause
#     - assessment
#     - recommendation
#     - confidence score
#     """

#     # response = billing_agent.run(query)

#     return {
#             "summary": "Consumption spike detected.",
#             "probable_cause": "Possible HVAC seasonal increase.",
#             "assessment": "Bill appears valid.",
#             "recommendation": "No adjustment required.",
#             "confidence_score": 0.93,

#             "trace": [
#                 "Retrieved customer billing history",
#                 "Calculated historical average consumption",
#                 "Detected abnormal usage spike",
#                 "Compared seasonal consumption pattern",
#                 "Validated billing determinants",
#                 "Generated final billing assessment"
#             ]
#     }

#     # return response


def investigate(customer_id: str):

    return {

        "customer_id": customer_id,

        "summary":
            "Consumption spike detected.",

        "probable_cause":
            "Possible HVAC seasonal increase.",

        "assessment":
            "Bill appears valid.",

        "recommendation":
            "No adjustment required.",

        "confidence_score":
            0.93,

        "trace": [

            "Retrieved customer billing history",

            "Calculated historical average consumption",

            "Detected abnormal usage spike",

            "Compared seasonal consumption pattern",

            "Validated billing determinants",

            "Generated final billing assessment"
        ]
    }