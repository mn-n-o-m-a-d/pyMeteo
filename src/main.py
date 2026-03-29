import requests
import json
import time
import datetime


def get_city_weather(lat, lon, name, timestamp):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()

        return {
            "name": name,
            "temp": data["current_weather"]["temperature"],
            "code": data["current_weather"]["weathercode"],
            "timestamp": timestamp,
        }
    except Exception as e:
        print(f"Error at {name}: {e}")
        return None


def get_forecast(lat, lon, name, timestamp):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        daily_data = data["daily"]
        forecast_days = []

        for i in range(len(daily_data["time"])):
            forecast_days.append(
                {
                    "date": daily_data["time"][i],
                    "code": daily_data["weather_code"][i],
                    "temp_max": daily_data["temperature_2m_max"][i],
                    "temp_min": daily_data["temperature_2m_min"][i],
                }
            )

        return {"name": name, "timestamp": timestamp, "forecast": forecast_days}
    except Exception as e:
        print(f"Error at {name}: {e}")
        return None


if __name__ == "__main__":
    cities = [
        (48.25, 16.36, "Wien"),
        (47.07, 15.44, "Graz"),
        (47.50, 9.74, "Bregenz"),
        (47.27, 11.40, "Innsbruck"),
        (47.80, 13.03, "Salzburg"),
        (48.31, 14.29, "Linz"),
        (48.20, 15.62, "St. Pölten"),
        (47.85, 16.52, "Eisenstadt"),
        (46.62, 14.31, "Klagenfurt"),
    ]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    all_weather = []
    for lat, lon, name in cities:
        weather = get_forecast(lat, lon, name, now)
        if weather:
            all_weather.append(weather)
        time.sleep(0.1)

    with open(
        "/home/manuel/VSCode/2026/pyMeteo/frontend/austria_weather.json", "w"
    ) as f:
        json.dump(all_weather, f)

    print(f"{len(all_weather)} Cities updated.")
