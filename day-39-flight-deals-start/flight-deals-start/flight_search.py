import requests
import datetime as dt
from flight_data import FlightData
import os

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_HEADERS = {
    "apikey": TEQUILA_API_KEY,
}
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
FLY_FROM_IATA = "LON"
FLY_FROM_NAME = "London"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.iata_code = "TESTING"

    def get_iata_code(self, city_name):
        params = {
            "term": city_name,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}locations/query", params=params, headers=TEQUILA_HEADERS)
        response.raise_for_status()
        data = response.json()
        iata_code = data["locations"][0]["code"]
        # print(iata_code)
        return iata_code

    def search_for_flights(self, iata):
        today = dt.datetime.now()
        tomorrow = today + dt.timedelta(days=2)
        tomorrow_plus_six_months = tomorrow + dt.timedelta(days=180)

        params = {
            "fly_from": FLY_FROM_IATA,
            "fly_to": iata,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": tomorrow_plus_six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}search", params=params, headers=TEQUILA_HEADERS)

        # print(data)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {iata}")
            return None

        # outbound = data[0]["local_departure"].split("T")
        # outbound = outbound[0]
        # inbound = data[0]["local_arrival"].split("T")
        # inbound = inbound[0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

