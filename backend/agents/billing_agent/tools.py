import pandas as pd
from langchain.tools import tool

billing_df = pd.read_csv(
    "sample_data/billing_data.csv"
)

@tool
def get_customer_history(customer_id: str):
    """
    Returns billing history for customer.
    """

    customer_data = billing_df[
        billing_df["customer_id"] == customer_id
    ]

    return customer_data.to_json(
        orient="records"
    )


@tool
def get_latest_bill(customer_id: str):
    """
    Returns latest billing record.
    """

    customer_data = billing_df[
        billing_df["customer_id"] == customer_id
    ]

    latest = customer_data.iloc[-1]

    return latest.to_json()


@tool
def detect_abnormal_usage(customer_id: str):
    """
    Detects abnormal consumption spikes.
    """

    customer_data = billing_df[
        billing_df["customer_id"] == customer_id
    ]

    avg = customer_data[
        "consumption_kwh"
    ].mean()

    latest = customer_data.iloc[-1]

    spike_pct = (
        (
            latest["consumption_kwh"] - avg
        ) / avg
    ) * 100

    return {
        "average_consumption": round(avg, 2),
        "latest_consumption": latest[
            "consumption_kwh"
        ],
        "spike_percentage": round(spike_pct, 2)
    }