# API for Onboarding Customer Risk Score and Rating

1. Please send GET request to endpoint /crs. 
2. Required schema for clients' request:

        {"user_id": "A1234",
        "KYC": [{"GEOGRAPHY": "A",
                "SOF": "B", 
                "POA": "C"}]}
3. Response:

    {
	"Risk_Rating": Low/Medium/High :: String,
	"Risk_Score": Customer Risk Score :: Integer,
	"User_ID": User ID :: String
    }