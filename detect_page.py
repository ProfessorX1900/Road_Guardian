import streamlit as st
import torch
from PIL import Image

@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./Model/best.pt')  
    model.conf = 0.80
    return model

model = load_model()

def detect_page():
    with open('./css/detect.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("""<div class="hero">
                    <div class="title">AI Pothole Detective 🕵️‍♂️</div>
                    <div class="subtitle">Upload an image and let our AI do the detective work!</div>
                </div>""", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-box">
            <h3>How It Works</h3>
            <ol>
                <li>Upload a clear image of the road surface.</li>
                <li>Click the "Detect Potholes" button to activate our AI.</li>
                <li>Our advanced algorithm will analyse the image for potholes.</li>
                <li>Results will be displayed, highlighting any detected potholes.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    detect_button = st.button("Detect Potholes")

    st.markdown(
        """
        <div class="info-box">
            <h3>Tips for Best Results</h3>
            <ul>
                <li>Ensure good lighting conditions when taking the photo.</li>
                <li>Try to capture the entire pothole and some surrounding road.</li>
                <li>Avoid blurry or out-of-focus images for accurate detection.</li>
                <li>If possible, take the photo from directly above the pothole.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            <p>Developed with ❤️ by Road Guardian</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if uploaded_file is not None and detect_button:
        image = Image.open(uploaded_file)
        results = model(image)
        st.image(results.render()[0], channels="BGR", caption="Uploaded Image with Detections")
