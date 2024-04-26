import requests
from pprint import pprint
import os
from flight_search import FlightSearch

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/f58e8d4fb7e4229cf93e6d95ad58f877/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self, data):
        for item in self.destination_data:
            row_number = int(item["id"])
            endpoint = f"{SHEETY_ENDPOINT}/{row_number}"
            new_data = {
                "price": {
                    "iataCode": item["iataCode"],
                }
            }
            response = requests.put(url=endpoint, json=new_data, headers=SHEETY_HEADERS)
            response.raise_for_status()
