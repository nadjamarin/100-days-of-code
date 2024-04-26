#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

DEPARTURE_NAME = "London"
DEPARTURE_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(f"This is the data:\n{sheet_data}")

flight_search = FlightSearch()

# Add IATA codes to sheet data
# for item in sheet_data:
#     item["iataCode"] = flight_search.get_iata_code(item["city"])

pprint(f"This is the new data:\n{sheet_data}")

data_manager.destination_data = sheet_data
# data_manager.update_data(sheet_data)

flight_data = {}
for item in sheet_data:
    flight_data[item["city"]] = flight_search.search_for_flights(item["iataCode"])
    # prices[item["city"]] = flight_search.search_for_flights(item["iataCode"])
    # if prices[item["city"]] < item["lowestPrice"]:
    #     print(f"low price flight to {item['city']}")
    # else:
    #     print(f"no low price flight to {item['city']}")



