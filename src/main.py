import requests
import json
import os

def update_weather(lat, lon, name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()

        # file_path = "/var/www/html/weather.json"
        file_path = f"/home/mn/VSCode/pyMeteo/{name}.json"

        with open(file_path, "w") as f:
            json.dump(data["current_weather"], f)

        print("Weather data reloaded.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_weather(48.25, 16.36, "Wien")
    update_weather(47.07, 15.43, "Graz")
    update_weather(47.50, 9.74, "Bregenz")
    update_weather(47.27, 11.40, "Innsbruck")
    update_weather(47.80, 13.03, "Salzburg")
    update_weather(48.31, 14.29, "Linz")
    update_weather(48.20, 15.62, "StPölten")
    update_weather(47.85, 16.52, "Eisenstadt")
    update_weather(46.62, 14.31, "Klagenfurt")
