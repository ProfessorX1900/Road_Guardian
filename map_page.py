import streamlit as st
import pydeck as pdk
import pandas as pd
import os

def initialize_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w') as file:
            file.write("Suburb,Latitude,Longitude\n")

initialize_csv("./data/pothole_locations.csv")

def load_pothole_data():
    try:
        return pd.read_csv("./data/pothole_locations.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Suburb", "Latitude", "Longitude"])

def map_page():
    with open('./css/map_page_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    df = pd.read_csv("./data/sydney_suburbs.csv")
    pothole_df = load_pothole_data()

    st.markdown("""<div class="map-container">
                    <div class="map-title">Pothole Detection Map 🌿</div>
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="search-container">
                    <div class="map-subtitle">Explore Potholes around Sydney</div>
                </div>""", unsafe_allow_html=True)

    search_term = st.text_input("Enter a suburb name:", "")

    if search_term:
        selected_suburb = df[df['Suburb'].str.contains(search_term, case=False)]
        if not selected_suburb.empty:
            selected_lat = selected_suburb['Latitude'].values[0]
            selected_lon = selected_suburb['Longitude'].values[0]
            initial_view_state = pdk.ViewState(latitude=selected_lat, longitude=selected_lon, zoom=14)
        else:
            st.error("Suburb not found.")
            initial_view_state = pdk.ViewState(latitude=-33.8688, longitude=151.2093, zoom=9)
    else:
        initial_view_state = pdk.ViewState(latitude=-33.8688, longitude=151.2093, zoom=9)

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=pothole_df,
        get_position=['Longitude', 'Latitude'],
        get_color=[200, 30, 0, 160],
        get_radius=5,
    )

    st.pydeck_chart(
        pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=initial_view_state,
            layers=[layer],
            tooltip={"text": "Suburb: {Suburb}\nLatitude: {Latitude}\nLongitude: {Longitude}"}
        )
    )

    st.markdown('<div class="search-container"><h3>How to Use the Pothole Explorer</h3></div>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>🔍 Search for a specific suburb using the search bar above.</li>
        <li>🖱️ Click and drag to pan around the map.</li>
        <li>⚫ Red dots indicate reported potholes.</li>
        <li>👆 Click on a dot to view more details about the reported pothole.</li>
        <li>🔎 Use the zoom controls to get a closer look at specific areas.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="footer">
            <p>Developed with ❤️ by Road Guardian</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    map_page()