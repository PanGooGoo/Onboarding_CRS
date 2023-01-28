from flask import Flask, request

ENCODER = [
    {
        "GEOGRAPHY": {"A": "Low", "B": "Medium", "C": "High"},
        "SOF": {"A": "Low", "B": "Medium", "C": "High"},
        "POA": {"A": "Low", "B": "Medium", "C": "High"},
    }
]

CRR_CATEGORICAL = [
    {
        "GEOGRAPHY": {"Low": 1, "Medium": 5, "High": 20},
        "SOF": {"Low": 1, "Medium": 5, "High": 20},
        "POA": {"Low": 1, "Medium": 5, "High": 20},
    }
]

app = Flask(__name__)


@app.get("/crs")
def get_customer_risk_score():
    user_data = request.get_json()

    GEOGRAPHY = user_data["KYC"][0]["GEOGRAPHY"]
    SOF = user_data["KYC"][0]["SOF"]
    POA = user_data["KYC"][0]["POA"]

    GEOGRAPHY_to_points = CRR_CATEGORICAL[0]["GEOGRAPHY"][
        ENCODER[0]["GEOGRAPHY"][GEOGRAPHY]
    ]
    SOF_to_points = CRR_CATEGORICAL[0]["SOF"][ENCODER[0]["SOF"][SOF]]
    POA_to_points = CRR_CATEGORICAL[0]["POA"][ENCODER[0]["POA"][POA]]
    RS = GEOGRAPHY_to_points + SOF_to_points + POA_to_points

    if RS >= 50:
        return (
            {"User_ID": user_data["user_id"], "Risk_Score": RS, "Risk_Rating": "High"},
            201,
        )
    elif RS >= 20 and RS < 50:
        return (
            {
                "User_ID": user_data["user_id"],
                "Risk_Score": RS,
                "Risk_Rating": "Medium",
            },
            201,
        )
    else:
        return (
            {"User_ID": user_data["user_id"], "Risk_Score": RS, "Risk_Rating": "Low"},
            201,
        )
