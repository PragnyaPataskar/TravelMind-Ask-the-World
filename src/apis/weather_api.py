import requests

def get_weather(city):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo = requests.get(url, timeout=10).json()
        if "results" not in geo or not geo["results"]:
            return {"error": "City not found"}
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        data = requests.get(weather_url, timeout=10).json()
        return data.get("current_weather", {})
    except requests.Timeout:
        return {"error": "Weather API timed out. Please try again later."}
    except Exception as e:
        return {"error": f"Weather API error: {e}"}