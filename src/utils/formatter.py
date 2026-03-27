import json

def format_response(response):
    try:
        if isinstance(response, str):
            return json.loads(response)
        return response
    except:
        return {
            "summary": str(response),
            "weather": None,
            "air_quality": None,
            "places": []
        }