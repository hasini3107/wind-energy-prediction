import streamlit as st
import numpy as np
import joblib
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Wind Energy Prediction 🌬️",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- BACKGROUND + STYLING ----------------
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    /* Background animation */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: 110%;
        background-position: center;
        animation: moveBg 30s linear infinite;
    }}

    @keyframes moveBg {{
        0% {{ background-position: center top; }}
        50% {{ background-position: center center; }}
        100% {{ background-position: center top; }}
    }}

    /* Glass effect */
    .glass {{
        background: rgba(0, 0, 0, 0.55);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 0 25px rgba(0,255,204,0.3);
    }}

    /* Buttons */
    div.stButton > button {{
        background: linear-gradient(135deg, #00ffcc, #0077ff);
        color: black;
        font-size: 18px;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
    }}
    div.stButton > button:hover {{
        transform: scale(1.05);
    }}

    /* Sidebar width */
    section[data-testid="stSidebar"] {{
        width: 220px !important;
    }}

    /* Input label text */
    label {{
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }}

    /* Input box text */
    input {{
        font-size: 18px !important;
        color: #ffffff !important;
    }}

    /* Input box background */
    div[data-baseweb="input"] {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_background("fans.jpg")

# ---------------- BACKGROUND SOUND ----------------
st.audio("fan_sound.wav.wav", autoplay=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="glass">
    <h1 style="text-align:center; color:#E0FFFF;">🌬️ Wind Energy Prediction 🍃</h1>
    <h4 style="text-align:center; color:white;">Predicting electricity generation using Machine Learning</h4>
    <h3 style="text-align:center; color:#00FFCC;">Developed by Hasini</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- LOAD MODEL ----------------
model = joblib.load("polynomial_regression_model.pkl")
scaler = joblib.load("scaler.pkl")
poly = joblib.load("poly_features.pkl")

# ---------------- INPUT SECTION ----------------
st.markdown("""
<div class="glass">
    <h2 style="color:#E0FFFF;">🔢 Enter Wind Parameters</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    wind_speed = st.number_input("🌬️ Wind Speed (m/s)", 0.0, 50.0, 7.5)
with col2:
    wind_direction = st.number_input("🧭 Wind Direction (°)", 0.0, 360.0, 180.0)
with col3:
    theoretical_power = st.number_input("⚡ Theoretical Power Curve (kWh)", 0.0, 5000.0, 1200.0)

# ---------------- PREDICTION ----------------
st.write("")
if st.button("🔮 Predict Power Output"):
    new_data = np.array([[wind_speed, wind_direction, theoretical_power]])
    new_data_scaled = scaler.transform(new_data)
    new_data_poly = poly.transform(new_data_scaled)
    prediction = model.predict(new_data_poly)

    st.markdown(f"""
    <div class="glass" style="text-align:center;">
        <h2 style="color:#00FFCC;">⚡ Predicted LV Active Power</h2>
        <h1 style="color:white;">{prediction[0]:.2f} kW</h1>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center; color:white;">🌱 Renewable Energy | Machine Learning | Streamlit</p>
""", unsafe_allow_html=True)
