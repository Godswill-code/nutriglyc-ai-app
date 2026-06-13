import streamlit as st
import pandas as pd
import joblib

# Load model and training columns
model = joblib.load("best_glucose_spike_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(
    page_title="NutriGlyc AI",
    page_icon="🩺",
    layout="centered"
)

st.title("NutriGlyc AI: Glucose Spike Prediction")
st.write(
    "This app predicts the risk of a post-meal glucose spike using patient, meal, clinical, and lifestyle information."
)

st.warning(
    "Disclaimer: This tool is for educational and decision-support purposes only. It is not a medical diagnosis tool."
)

# ----------------------------
# User Inputs
# ----------------------------

st.header("Patient Information")

age = st.number_input("Age", min_value=18, max_value=100, value=45)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=27.0)
diabetes_type = st.selectbox("Diabetes Type", ["Type 1", "Type 2"])

st.header("Meal Information")

meal_time = st.selectbox("Meal Time", ["Breakfast", "Lunch", "Dinner", "Snack"])
carb_intake = st.number_input("Carbohydrate Intake (g)", min_value=0.0, max_value=400.0, value=120.0)
protein_intake = st.number_input("Protein Intake (g)", min_value=0.0, max_value=200.0, value=60.0)
fat_intake = st.number_input("Fat Intake (g)", min_value=0.0, max_value=200.0, value=50.0)
fiber_intake = st.number_input("Fibre Intake (g)", min_value=0.0, max_value=100.0, value=18.0)
sugar_intake = st.number_input("Sugar Intake (g)", min_value=0.0, max_value=200.0, value=45.0)
glycemic_index = st.number_input("Glycemic Index", min_value=0.0, max_value=100.0, value=60.0)
portion_size = st.number_input("Portion Size (g)", min_value=0.0, max_value=1000.0, value=400.0)
water_intake = st.number_input("Water Intake (ml)", min_value=0.0, max_value=1000.0, value=250.0)

st.header("Clinical and Lifestyle Information")

insulin_dose = st.number_input("Insulin Dose", min_value=0.0, max_value=100.0, value=10.0)
medication_adherence = st.selectbox("Medication Adherence", [0, 1])
physical_activity = st.number_input("Physical Activity", min_value=0.0, max_value=200.0, value=45.0)
stress_level = st.number_input("Stress Level", min_value=1.0, max_value=10.0, value=5.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=12.0, value=6.5)
pre_meal_glucose = st.number_input("Pre-meal Glucose", min_value=50.0, max_value=250.0, value=110.0)
smoking_status = st.selectbox("Smoking Status", ["No", "Yes"])
alcohol_consumption = st.selectbox("Alcohol Consumption", ["No", "Yes"])

# ----------------------------
# Feature Engineering
# ----------------------------

glycemic_load = (carb_intake * glycemic_index) / 100
carb_fiber_ratio = carb_intake / (fiber_intake + 1)
meal_risk_score = glycemic_load / (fiber_intake + 1)

protein_carb_ratio = protein_intake / (carb_intake + 1)
fat_carb_ratio = fat_intake / (carb_intake + 1)
sugar_carb_ratio = sugar_intake / (carb_intake + 1)
sleep_stress_score = sleep_hours / (stress_level + 1)
activity_bmi_ratio = physical_activity / (bmi + 1)
hydration_activity_ratio = water_intake / (physical_activity + 1)
carb_portion_ratio = carb_intake / (portion_size + 1)
glucose_risk_index = pre_meal_glucose + glycemic_load + meal_risk_score

# ----------------------------
# Create Input DataFrame
# ----------------------------

input_data = pd.DataFrame([{
    "age": age,
    "gender": gender,
    "bmi": bmi,
    "diabetes_type": diabetes_type,
    "meal_time": meal_time,
    "carb_intake": carb_intake,
    "protein_intake": protein_intake,
    "fat_intake": fat_intake,
    "fiber_intake": fiber_intake,
    "sugar_intake": sugar_intake,
    "glycemic_index": glycemic_index,
    "portion_size": portion_size,
    "water_intake": water_intake,
    "insulin_dose": insulin_dose,
    "medication_adherence": medication_adherence,
    "physical_activity": physical_activity,
    "stress_level": stress_level,
    "sleep_hours": sleep_hours,
    "pre_meal_glucose": pre_meal_glucose,
    "smoking_status": smoking_status,
    "alcohol_consumption": alcohol_consumption,
    "glycemic_load": glycemic_load,
    "carb_fiber_ratio": carb_fiber_ratio,
    "meal_risk_score": meal_risk_score,
    "protein_carb_ratio": protein_carb_ratio,
    "fat_carb_ratio": fat_carb_ratio,
    "sugar_carb_ratio": sugar_carb_ratio,
    "sleep_stress_score": sleep_stress_score,
    "activity_bmi_ratio": activity_bmi_ratio,
    "hydration_activity_ratio": hydration_activity_ratio,
    "carb_portion_ratio": carb_portion_ratio,
    "glucose_risk_index": glucose_risk_index
}])

# One-hot encode categorical variables
input_data = pd.get_dummies(input_data)

# Align columns with training data
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict Glucose Spike Risk"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"High glucose spike risk detected. Probability: {probability:.2%}")
    else:
        st.success(f"Low glucose spike risk detected. Probability: {probability:.2%}")

    st.subheader("Personalised Nutrition Insight")

    if carb_intake > 150:
        st.warning("Carbohydrate intake is high. Consider reducing carbohydrate portion size.")
    elif carb_intake > 100:
        st.info("Carbohydrate intake is moderate. Consider balancing it with fibre and protein.")
    else:
        st.success("Carbohydrate intake appears controlled.")

    if glycemic_load > 90:
        st.warning("Glycemic load is high. Consider choosing lower glycemic load foods.")
    elif glycemic_load > 60:
        st.info("Glycemic load is moderate. Monitor portion size and carbohydrate quality.")
    else:
        st.success("Glycemic load appears low.")

    if fiber_intake < 10:
        st.warning("Fibre intake is low. Consider adding vegetables, beans, oats, or whole grains.")
    else:
        st.success("Fibre intake appears reasonable.")

    if physical_activity < 30:
        st.warning("Physical activity is low. A short walk after meals may support glucose control.")
    else:
        st.success("Physical activity level appears supportive.")

    st.subheader("Calculated Meal Risk Features")

    st.write("Glycemic Load:", round(glycemic_load, 2))
    st.write("Carb-Fibre Ratio:", round(carb_fiber_ratio, 2))
    st.write("Meal Risk Score:", round(meal_risk_score, 2))
    st.write("Protein-Carb Ratio:", round(protein_carb_ratio, 2))