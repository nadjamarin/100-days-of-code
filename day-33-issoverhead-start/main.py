import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 39.758949  # Your latitude
MY_LONG = -84.191605  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
# iss_latitude = 39.1
# iss_longitude = -84.2


# Your position is within +5 or -5 degrees of the ISS position.
def iss_is_overhead():
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now()
    hour_now = int(time_now.hour)
    # hour_now = 1

    if sunrise >= hour_now >= sunset:
        return True

# run the code every 60 seconds
while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        my_email = "nmsparkles@gmail.com"
        password = "tqbh bgpz kboa lenq"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS is Overhead!\n\nLook up! The ISS is above you in the sky!")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
