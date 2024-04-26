import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

exercises_done = input("Tell me which exercises you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_params = {
    "query": exercises_done,
    "gender": "female",
    "weight_kg": 61.2,
    "height_cm": 162.56,
    "age": 25,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
response.raise_for_status()
response_json = response.json()

today = dt.datetime.now()
today_date = today.strftime("%m/%d/%Y")
today_time = today.strftime("%I:%M")

exercise_name = response_json["exercises"][0]["name"]
duration_of_exercise = response_json["exercises"][0]["duration_min"]
calories_burned = response_json["exercises"][0]["nf_calories"]

exercise_data = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise_name.title(),
        "duration": duration_of_exercise,
        "calories": calories_burned,
    }
}

sheety_headers = {
    "Authorization": SHEETY_TOKEN,
}
sheety_endpoint = "https://api.sheety.co/f58e8d4fb7e4229cf93e6d95ad58f877/myWorkouts/workouts"
sheety_response = requests.post(url=sheety_endpoint, json=exercise_data, headers=sheety_headers)
