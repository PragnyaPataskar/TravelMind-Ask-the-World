# TravelMind: Ask the World

This repo iy part of my portfolio work and learning, which contains the code for for Retrieval-Augmented Generation (RAG) chatbot that answers the question like Air quality, Places to visit, Interactive map, Summarized travel info and traveling guide throughout the World.

All responses are structured in JSON and visualized in a Streamlit UI.

## Features

- Natural language travel Q&A
- Weather and air quality from Open-Meteo
- Wikipedia-powered place search (RAG)
- Interactive maps (folium + streamlit-folium)
- Robust error handling and user-friendly messages
- JSON and card-based UI

## How To Run

Clone the repo:  git clone https://github.com/Username/TravelMind-Ask-the-World.git
cd TravelMind_Ask the World
Install dependencies
pip install -r requirements.txt

 Set your API keys in a `.env` file.


## Runing the app :

streamlit run app.py
Open the link shown in your terminal (default: http://localhost:8501)

## Input

Ask questions like:
- "What is the weather in Paris?"
- "Best vegetarian restaurants in Aachen?"
- "Air quality in Delhi now?"

## Project Structure

- `app.py` — Streamlit UI
- `src/agents/agent.py` — Agent setup and system prompt
- `src/agents/tools.py` — Tool definitions (weather, air quality, wiki, geocoding)
- `src/apis/` — API integrations
- `src/rag/` — Retrieval-augmented generation (RAG) logic

## Sources

- https://docs.langchain.com/oss/python/langchain/agents
- https://console.groq.com/docs/models
- https://docs.langchain.com/oss/python/langchain/rag