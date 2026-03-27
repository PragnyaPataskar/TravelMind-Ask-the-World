
from langchain_community.tools import Tool
from src.apis.weather_api import get_weather
from src.apis.air_quality_api import get_air_quality
from src.rag.retriever import get_retriever
from src.apis.geocoding_api import get_coordinates

retriever = get_retriever()

def wiki_search(query):
    docs = retriever.invoke(query)
    if not docs:
        return "No info found."
    if isinstance(docs, list):
        return [doc.page_content[:300] for doc in docs]
    else:
        return docs.page_content[:300]

tools = [
    Tool(
        name="Weather",
        func=get_weather,
        description="Get current weather for a city"
    ),
    Tool(
        name="AirQuality",
        func=get_air_quality,
        description="Get air quality data for a city"
    ),
    Tool(
        name="WikipediaSearch",
        func=wiki_search,
        description="Search travel info about a place"
    ),
]

tools.append(
    Tool(
        name="Geocoding",
        func=get_coordinates,
        description="Get latitude and longitude of a city"
    )
)