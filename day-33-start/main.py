import requests
from datetime import datetime
MY_LAT = 39.758949
MY_LONG = -84.191605

# International Space Station API (http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
# # response will not be in JSON format, so we need to access the data another way
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # Printing response gives a response code
# # print(response)
# # print(response.status_code)
#
# # Automatically generate exceptions
# response.raise_for_status()
#
# # Get JSON data from response
# # Can use keys to get specific pieces of data
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# # print(data)
#
# iss_position = (longitude, latitude)
# print(iss_position)



# Sunrise and sunset times (https://sunrise-sunset.org/api)
# parameters must match name and format from the API documentation
# list parameters in a dictionary
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# This API has 2 required parameters: longitude and latitude
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
# sunrise format does not match time_now format, so need to change formatted parameter in the API request^
print(time_now.hour)

# Reformat sunrise using split() to remove extra characters and partition the data
# Get just the hour (24 hour clock)
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
