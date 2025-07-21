import streamlit as st
import pickle
import numpy as np
import base64

# Load model
with open('insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to set image as background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/avif;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set new AVIF background
add_bg_from_local("/content/medical _insurance_backgroud_image.avif")

# Banner Section
st.markdown(
    """
    <div style='background-color:#007ACC; padding: 20px; border-radius: 10px; margin-bottom: 30px;'>
        <h1 style='color:white; text-align:center;'>Medical Insurance Claim Prediction</h1>
        <p style='color:white; text-align:center;'>Predict your estimated insurance charges using ML</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input Form
age = st.number_input("Enter Age", min_value=0, max_value=100)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI (Body Mass Index)", 0.0, 100.0, 20.0)
children = st.number_input("Number of Children", min_value=0, max_value=10)
smoker = st.selectbox("Smoker?", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Encode input
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_encoded = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}[region]

# Prediction Button
if st.button("Predict"):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Insurance Charges: ₹{prediction:,.2f}")
