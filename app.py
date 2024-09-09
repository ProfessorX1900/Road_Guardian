import streamlit as st

st.set_page_config(page_title='Pothole Detection', page_icon="🚧", layout="wide")

with open('./css/Global_styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

from home import home_page
from map_page import map_page
from report_page import report_page
from detect_page import detect_page

tabs = ["Home", "Map", "Report Pothole", "Pothole Detection"]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab == "Home":
    home_page()
elif selected_tab == "Map":
    map_page()
elif selected_tab == "Report Pothole":
    report_page()
elif selected_tab == "Pothole Detection":
    detect_page()