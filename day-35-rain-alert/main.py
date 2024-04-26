import requests
import os
from twilio.rest import Client

LAT = 39.758949
LONG = -84.191605

# Open Weather API info
api_key = os.environ.get("API_KEY")
# Twilio account info
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
# https://api.openweathermap.org/data/2.5/weather?q=Dayton,OH,US&appid=2cc6188ca9fac0f398879b1c31cd98bb

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()


def check_ids(id_list, value):
    for w_id in id_list:
        if value > w_id:
            return True
    return False


weather_ids = []
for hour_data in data["list"]:
    # weather_id = data["list"][index]["weather"][0]["id"]
    weather_id = hour_data["weather"][0]["id"]
    weather_ids.append(weather_id)

if check_ids(weather_ids, 700):
    print("Bring an umbrella.")
else:
    print("Do not bring an umbrella.")

# Send yourself an SMS message
# if check_ids(weather_ids, 700):
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an umbrella!",
#         from_='+18445800618',
#         to='+19378251525'
#     )
#     print(message.status)
