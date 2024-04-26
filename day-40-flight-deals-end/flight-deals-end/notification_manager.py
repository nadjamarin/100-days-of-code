from twilio.rest import Client
import smtplib
import requests
import os
from pprint import pprint

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRT_NUM")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VER_NUM")

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/f58e8d4fb7e4229cf93e6d95ad58f877/flightDeals/users"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,
}

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message):
        # Get emails from Google sheet with Sheety
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        # print(data)
        users = data["users"]
        for user in users:
            to_email = user["email"]
            my_email = EMAIL
            password = PASSWORD

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=to_email,
                                    msg=f"Subject: Low Price Flight Alert!\n\n{message}")
