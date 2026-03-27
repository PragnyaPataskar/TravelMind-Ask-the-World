import requests

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    res = requests.get(url).json()

    if "results" not in res:
        return {"error": "City not found"}

    return {
        "latitude": res["results"][0]["latitude"],
        "longitude": res["results"][0]["longitude"],
        "name": res["results"][0]["name"]
    }