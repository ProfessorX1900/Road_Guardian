import streamlit as st
import pandas as pd
import torch
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./Model/best.pt')
    model.conf = 0.80 
    return model

model = load_model()

def get_image_coordinates(image):
    exif_data = image._getexif()
    if not exif_data:
        return None

    gps_info = {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_info[sub_decoded] = value[t]

    if not gps_info:
        return None

    def convert_to_degrees(value):
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)

    lat = convert_to_degrees(gps_info['GPSLatitude'])
    if gps_info['GPSLatitudeRef'] != "N":
        lat = -lat

    lon = convert_to_degrees(gps_info['GPSLongitude'])
    if gps_info['GPSLongitudeRef'] != "E":
        lon = -lon

    return lat, lon

def save_pothole_location(suburb, latitude, longitude):
    data = {"Suburb": suburb, "Latitude": latitude, "Longitude": longitude}
    df = pd.DataFrame([data])
    df.to_csv("./data/pothole_locations.csv", mode='a', header=not os.path.isfile("./data/pothole_locations.csv"), index=False)

def initialize_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w') as file:
            file.write("Suburb,Latitude,Longitude\n")

initialize_csv("./data/pothole_locations.csv")

def report_page():
    with open('./css/report.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("""<div class="title-container">
                    <div class="title">Report a Pothole 🚧</div>
                <div class="subtitle">Help improve road safety by reporting potholes in your area</div>
                </div>""", unsafe_allow_html=True)

    with st.container():
        st.markdown(
            """
            <div class="form-container">
                <h3>Submit Your Report</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("pothole_form"):
            uploaded_file = st.file_uploader("Upload an image of the pothole", type=["jpg", "png", "jpeg"])
            submitted = st.form_submit_button("Submit Report")

            if submitted:  
                if uploaded_file:
                    image = Image.open(uploaded_file)
                    results = model(image)

                    detections = results.pandas().xyxy[0]

                    detected_pothole = False
                    for index, detection in detections.iterrows():
                        if detection['name'] == 'Pothole' and detection['confidence'] > model.conf:
                            detected_pothole = True
                            break

                    if detected_pothole:
                        coords = get_image_coordinates(image)
                        if coords:
                            latitude, longitude = coords
                            st.success(f"Pothole detected and reported at coordinates: Latitude {latitude}, Longitude {longitude}")
                            save_pothole_location("Unknown", latitude, longitude)  # Added "Unknown" as a placeholder for suburb
                        else:
                            st.error("No GPS coordinates found in the image.")
                    else:
                        st.error("No pothole detected in the image.")

                    st.image(results.render()[0], channels="BGR", caption="Uploaded Image with Detections")
                else:
                    st.warning("Please fill out all fields and upload an image.")


    st.markdown("""
    <div class="info-box">
            <h3>Tips for Effective Reporting</h3>
    </div>
    <ul>
        <li>📸 Take a clear, well-lit photo of the pothole.</li>
        <li>📍 Include nearby landmarks or street signs in your description for easier location.</li>
        <li>📏 Try to estimate the size of the pothole (e.g., diameter, depth).</li>
        <li>🚗 Mention any immediate safety concerns if applicable.</li>
        <li>🕒 Report potholes as soon as you notice them for quicker action.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown(
        """
        <div class="footer">
            <p>Developed with ❤️ by Road Guardian</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    report_page()
