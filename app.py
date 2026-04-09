import streamlit as st

st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=0.0)
height = st.number_input("Enter your height (meters):", min_value=0.0)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.error("Height must be greater than 0")
