import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user: only need to run this once
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Only need to create the graph once
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# URL to access your graph:
# f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"

# Post a pixel to the graph using a post request
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date and reformat it using strftime()
today = datetime.now()
# Can change the date if you want to log a pixel on another day
# today = datetime(year=2024, month=4, day=5)
today_formatted = today.strftime("%Y%m%d")

pixel_data = {
    "date": today_formatted,
    "quantity": "2",
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_params, headers=headers)

# Put and delete requests
# put(): change an existing pixel's value
pixel_change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

pixel_change_data = {
    "quantity": "3",
}

# response = requests.put(url=pixel_change_endpoint, json=pixel_change_data, headers=headers)

# delete(): delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
