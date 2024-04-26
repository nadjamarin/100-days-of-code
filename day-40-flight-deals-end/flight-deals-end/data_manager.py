from pprint import pprint
import requests
import os

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f58e8d4fb7e4229cf93e6d95ad58f877/flightDeals/prices"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
    # "Bearer DSsdkjnxcvkj443sdffs"
SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
