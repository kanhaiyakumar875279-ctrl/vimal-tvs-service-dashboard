
import pandas as pd
from datetime import datetime
import requests

# =====================
# EXOTEL CONFIG (FILL THESE)
# =====================
EXOTEL_SID = "YOUR_EXOTEL_SID"
API_KEY = "YOUR_API_KEY"
API_TOKEN = "YOUR_API_TOKEN"
EXOPHONE = "YOUR_EXOPHONE_NUMBER"
IVR_ID = "YOUR_IVR_ID"  # Exotel dashboard IVR ID

# =====================
# LOAD SERVICE DATA
# =====================
def get_service_due():
    df = pd.read_excel("service_data.xlsx")
    df['last_service_date'] = pd.to_datetime(df['last_service_date'])
    df['days'] = (datetime.today() - df['last_service_date']).dt.days

    due = df[
        (df['days'] >= 30) |
        (df['free_service'] == 'Yes') |
        (df['km_run'] >= 2500)
    ]
    return due

# =====================
# MAKE EXOTEL CALL
# =====================
def make_call(customer_number):
    url = f"https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect.json"
    payload = {
        'From': customer_number,
        'To': IVR_ID,
        'CallerId': EXOPHONE
    }
    r = requests.post(url, data=payload, auth=(API_KEY, API_TOKEN))
    print(customer_number, r.status_code)

# =====================
# MAIN
# =====================
if __name__ == "__main__":
    customers = get_service_due()
    for _, row in customers.iterrows():
        make_call(row['mobile'])
