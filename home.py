import streamlit as st

def home_page():
    with open('./css/Home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Hero Section
    st.markdown(
        """
        <div class="hero">
            <div class="main-title">Road Guardian 🛡️</div>
            <div class="subtitle">Empowering communities for safer streets</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-container">
            <div class="bubble">
                <div class="section-title">🗺️ Explore & Report</div>
                <div class="section-text">
                    Navigate our interactive map to view reported potholes. 
                    Spot a new one? Easily report it with just a few clicks.
                    Your contributions make a real difference in road safety.
                </div>
            </div>
            <div class="bubble">
                <div class="section-title">🌳 Community Impact</div>
                <div class="section-text">
                    Every report matters. Your input helps prioritize repairs,
                    influences road maintenance decisions, and ultimately
                    creates safer streets for everyone in our community.
                </div>
            </div>
            <div class="bubble">
                <div class="section-title">📷 AI-Powered Detection</div>
                <div class="section-text">
                    Leverage cutting-edge AI to identify potential potholes.
                    Our smart detection system analyzes your photos,
                    making the reporting process even more accurate and efficient.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Scrolling Content (Image first, then pothole info)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:  # Image Section
            st.image('./photos/page.jpg')  
        with col2:  # Information Section
            st.markdown("### Why do potholes happen?")
            st.markdown("""
                **Causes:**
                - **Water Infiltration:** When water seeps into the ground beneath the road surface, it can weaken the underlying soil. This is particularly problematic during heavy rainfalls, which can erode the roadbed and reduce its structural integrity.
                - **Freeze-Thaw Cycles:** In colder climates, water that has infiltrated cracks in the road can freeze and expand. When it thaws, it contracts, creating stress on the road surface. Repeated freeze-thaw cycles can cause significant cracking and eventually lead to potholes.
                - **Traffic Stress:** Heavy traffic, especially from large vehicles such as trucks and buses, places immense stress on road surfaces. Over time, this constant pressure can exacerbate existing weaknesses in the road, leading to cracks and potholes.

                **Impacts:**
                - **Vehicle Damage:** Potholes can cause significant damage to vehicles, including punctured tires, bent rims, and damaged suspension systems. Repeated impacts can lead to costly repairs and reduced vehicle lifespan.
                - **Safety Risks:** Potholes pose serious safety risks. Drivers may need to swerve suddenly to avoid them, which can lead to loss of control or collisions with other vehicles or objects. Additionally, hitting a pothole can cause drivers to lose control, resulting in accidents and injuries.
                - **Increased Maintenance Costs:** Municipalities and road maintenance agencies face increased costs for road repairs and vehicle damage claims due to potholes. Effective reporting and timely repairs can help reduce these costs and improve overall road safety.
                - **Disruption of Traffic Flow:** Potholes can create disruptions in traffic flow, leading to congestion and delays. Proper maintenance and prompt reporting help ensure smoother traffic conditions and minimize disruptions.
                """)


    st.markdown("""<div class="bubble">
                <div class="section-title">Understanding Potholes</div>
                <div class="section-text">
                    Potholes are more than just inconveniences; they're symptoms of 
                road deterioration that can pose serious risks to vehicles and safety. 
                Formed by water penetration, freeze-thaw cycles, and traffic stress, 
                these depressions can range from minor annoyances to major hazards.
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)


    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("## How to Report a Pothole?")
            st.markdown("""
            Reporting a pothole is quick and easy. Follow these steps:

            1. **Open the App:** Launch our Road Guardian app on your smartphone.
            2. **Locate the Pothole:** Use the map feature to pinpoint the exact location of the pothole.
            3. **Tap 'Report':** Click on the 'Report' button to start the reporting process.
            4. **Provide Details:** Add a brief description of the pothole, including its approximate size and depth.
            5. **Upload a Photo:** If possible, take a photo of the pothole to assist repair crews in identifying and addressing the issue faster.
            """)
        with col2:  
            st.image('./photos/break.jpg')  

    st.markdown(
        """
        <div class="footer">
            <p>Developed with ❤️ by Road Guardian</p>
        </div>
        """,
        unsafe_allow_html=True
    )
