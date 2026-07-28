import streamlit as st
import pandas as pd
import joblib

st.title("Diabetes Prediction App")

model = joblib.load("logistic_model.pkl")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 1, 100, 25)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
smoking_history = st.selectbox(
    "Smoking History",
    ["never", "No Info", "current", "former", "ever", "not current"]
)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
HbA1c_level = st.number_input("HbA1c Level", 3.0, 15.0, 5.5)
blood_glucose_level = st.number_input("Blood Glucose Level", 50, 300, 100)

gender_map = {"Female": 0, "Male": 1, "Other": 2}
smoking_map = {
    "No Info": 0,
    "current": 1,
    "ever": 2,
    "former": 3,
    "never": 4,
    "not current": 5
}

input_data = pd.DataFrame([[
    gender_map[gender],
    age,
    hypertension,
    heart_disease,
    smoking_map[smoking_history],
    bmi,
    HbA1c_level,
    blood_glucose_level
]], columns=[
    "gender",
    "age",
    "hypertension",
    "heart_disease",
    "smoking_history",
    "bmi",
    "HbA1c_level",
    "blood_glucose_level"
])

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes")
