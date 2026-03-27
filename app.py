
import streamlit as st
from streamlit_folium import st_folium
import folium
from src.agents.agent import get_agent
from src.utils.formatter import format_response

st.set_page_config(page_title="TravelMind 🌍", layout="wide")
st.title("🌍 TravelMind: Ask the World")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

agent = get_agent()

def extract_location(data):
    # Try to extract lat/lon from dict or list of dicts
    if isinstance(data, dict):
        lat = data.get("latitude") or data.get("lat")
        lon = data.get("longitude") or data.get("lon")
        if lat and lon:
            return float(lat), float(lon)
    if isinstance(data, list):
        for item in data:
            loc = extract_location(item)
            if loc:
                return loc
    return None

query = st.chat_input("Ask about any place...")

if query:
    st.session_state.chat_history.append(("user", query))
    with st.spinner("Thinking..."):
        response = agent.run(query)
    st.session_state.chat_history.append(("bot", response))

for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        with st.chat_message("assistant"):
            import json
            # Try to display JSON if possible
            if isinstance(message, dict):
                st.json(message)
                # Map integration using geocoding if city present
                city = message.get("city")
                if city:
                    try:
                        from src.apis.geocoding_api import get_coordinates
                        coords = get_coordinates(city)
                        if coords and "latitude" in coords and "longitude" in coords:
                            m = folium.Map(location=[coords["latitude"], coords["longitude"]], zoom_start=13)
                            folium.Marker([coords["latitude"], coords["longitude"]], popup=city).add_to(m)
                            st.markdown("### 🗺️ Map")
                            st_folium(m, width=700, height=400)
                        else:
                            st.warning("Location not found for this city.")
                    except Exception as e:
                        st.warning(f"Error fetching location: {e}")
                # Expandable raw JSON
                with st.expander("Show raw JSON response"):
                    st.json(message)
            else:
                try:
                    data = json.loads(message)
                    st.json(data)
                    city = data.get("city")
                    if city:
                        try:
                            from src.apis.geocoding_api import get_coordinates
                            coords = get_coordinates(city)
                            if coords and "latitude" in coords and "longitude" in coords:
                                m = folium.Map(location=[coords["latitude"], coords["longitude"]], zoom_start=13)
                                folium.Marker([coords["latitude"], coords["longitude"]], popup=city).add_to(m)
                                st.markdown("### 🗺️ Map")
                                st_folium(m, width=700, height=400)
                            else:
                                st.warning("Location not found for this city.")
                        except Exception as e:
                            st.warning(f"Error fetching location: {e}")
                    with st.expander("Show raw JSON response"):
                        st.json(data)
                except Exception:
                    st.write(message)