import requests

def get_air_quality(city):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo = requests.get(url, timeout=10).json()
        if "results" not in geo or not geo["results"]:
            return {"error": "City not found"}
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=pm10,pm2_5"
        data = requests.get(aq_url, timeout=10).json()
        return data.get("hourly", {})
    except requests.Timeout:
        return {"error": "Air Quality API timed out. Please try again later."}
    except Exception as e:
        return {"error": f"Air Quality API error: {e}"}