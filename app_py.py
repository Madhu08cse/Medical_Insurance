import streamlit as st
import pickle
import numpy as np
with open('insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Medical Insurance Claim Prediction")
age = st.number_input("Enter Age", min_value=0, max_value=100)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI (Body Mass Index)")
children = st.number_input("Number of Children", min_value=0, max_value=10)
smoker = st.selectbox("Smoker?", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_encoded = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}[region]
if st.button("Predict"):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    prediction = model.predict(input_data)[0]
    st.success(f" Predicted Insurance Charges: ₹{prediction:,.2f}")
