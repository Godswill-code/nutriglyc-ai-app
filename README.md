# NutriGlyc AI: Glucose Spike Prediction App
NutriGlyc AI is a machine learning web application designed to predict the risk of post-meal glucose spikes using patient, clinical, dietary, and lifestyle information.

## Project Objective
The objective of this project is to support early identification of glucose spike risk and provide personalised nutrition recommendations based on predictive analytics.

## Machine Learning Workflow
The project followed a complete data science lifecycle:

- Data loading and inspection
- Data cleaning and missing value treatment
- Exploratory Data Analysis
- Feature engineering
- Leakage-free model development
- Hyperparameter tuning
- Model evaluation
- SHAP explainability
- Deployment using Streamlit

## Key Predictors
The most important predictors identified were:

- Carbohydrate intake
- Glycemic load
- Insulin dose
- Physical activity
- Meal risk score
- Carb-fibre ratio
- Diabetes type

## Models Used
- Logistic Regression
- Random Forest
- XGBoost

## Deployment
This app was deployed using Streamlit Community Cloud.

## Disclaimer
This application is for educational and decision-support purposes only. It is not intended to replace professional medical advice, diagnosis, or treatment.