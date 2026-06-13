# NutriGlyc AI Solutions: Predictive Analytics for Glucose Spike Risk Assessment

## Project Overview

NutriGlyc AI Solutions is a healthcare analytics project designed to support the early identification and prevention of post-meal glucose spikes through machine learning and nutrition intelligence. The project integrates demographic, clinical, dietary, and lifestyle data to predict glucose spike risk and generate actionable insights for personalised nutrition management.

The solution aims to demonstrate how predictive analytics and explainable artificial intelligence can contribute to preventive healthcare, improved patient engagement, and data-driven decision-making in diabetes management.

---

## Business Problem

Type 2 Diabetes continues to pose a significant public health challenge due to increasing prevalence, delayed diagnosis, unhealthy dietary behaviours, and limited access to preventive interventions. Traditional assessment approaches often rely on manual evaluation and reactive treatment strategies.

This project addresses the need for a proactive system capable of:

* Identifying individuals at risk of experiencing glucose spikes before they occur.
* Supporting healthcare professionals with predictive insights.
* Delivering personalised nutrition recommendations.
* Encouraging preventive lifestyle modifications.

---

## Project Objectives

The project was developed to achieve the following objectives:

* Develop machine learning models capable of predicting post-meal glucose spikes.
* Identify the key factors contributing to glucose spike occurrence.
* Generate personalised nutrition recommendations based on predictive insights.
* Compare the performance of multiple machine learning algorithms.
* Improve transparency through explainable artificial intelligence techniques.
* Prepare the solution for future deployment as a clinical decision-support tool.

---

## Dataset Description

The dataset consists of meal-based patient health records containing demographic, nutritional, behavioural, and clinical information.

Each observation represents a single patient-meal interaction and includes variables related to:

### Demographic Factors

* Age
* Gender
* Body Mass Index (BMI)

### Clinical Factors

* Diabetes Type
* Insulin Dose
* Pre-meal Glucose Level
* Medication Adherence

### Nutritional Factors

* Carbohydrate Intake
* Protein Intake
* Fat Intake
* Fibre Intake
* Sugar Intake
* Glycaemic Index
* Portion Size

### Lifestyle Factors

* Physical Activity
* Sleep Duration
* Stress Level
* Water Intake
* Smoking Status
* Alcohol Consumption

### Target Variable

* `glucose_spike`

  * 0 = No glucose spike
  * 1 = Glucose spike occurred

---

## Methodology

The project followed a structured end-to-end data science lifecycle.

### 1. Data Cleaning and Preprocessing

* Missing value assessment and treatment using median imputation.
* Duplicate record detection and removal.
* Validation of numerical ranges.
* One-hot encoding of categorical variables.
* Removal of data leakage variables (`post_meal_glucose` and `glucose_change`).
* Removal of patient identifiers to improve generalisability.

### 2. Exploratory Data Analysis (EDA)

EDA was performed to understand the distribution of variables and identify relationships with glucose spike occurrence.

Analyses included:

* Distribution plots
* Boxplots
* Count plots
* Correlation analysis
* Independent t-tests
* Chi-square tests of independence

---

## Feature Engineering

Several domain-informed features were created to improve predictive performance, including:

* Protein-to-Carbohydrate Ratio
* Fat-to-Carbohydrate Ratio
* Sugar-to-Carbohydrate Ratio
* Carbohydrate-to-Fibre Ratio
* Sleep-Stress Score
* Activity-BMI Ratio
* Meal Risk Score
* Glucose Risk Index
* Hydration-Activity Ratio
* Carbohydrate-Portion Ratio

---

## Machine Learning Models

Three supervised learning algorithms were developed and evaluated:

| Model               | Scaling Required |
| ------------------- | ---------------- |
| Logistic Regression | Yes              |
| Random Forest       | No               |
| XGBoost             | No               |

### Hyperparameter Tuning

GridSearchCV was applied to optimise model performance.

Tuned models included:

* Logistic Regression
* Random Forest
* XGBoost

Cross-validation was used to assess model stability and generalisability.

---

## Model Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

The target variable exhibited a relatively balanced class distribution; therefore, advanced resampling techniques such as SMOTE were not required.

---

## Explainable AI

To improve transparency and support healthcare decision-making, model explainability techniques were employed.

Methods included:

* Feature Importance Analysis
* SHAP (SHapley Additive Explanations)

These approaches helped identify the strongest contributors to glucose spike risk.

---

## Key Findings

The analysis identified several important predictors of glucose spike occurrence.

### Strongest Predictors

* Carbohydrate Intake
* Glycaemic Load
* Meal Risk Score
* Diabetes Type
* Insulin Dose
* Physical Activity

### Clinical Insights

* Higher carbohydrate consumption was associated with increased glucose spike risk.
* Meals with higher glycaemic loads contributed significantly to glucose dysregulation.
* Individuals with Type 2 Diabetes demonstrated greater susceptibility to glucose spikes.
* Lower physical activity levels were associated with poorer glycaemic outcomes.

---

## Nutrition Recommendations

Based on the findings, the following strategies were recommended:

* Moderate total carbohydrate intake.
* Prioritise lower glycaemic load meals.
* Increase dietary fibre consumption.
* Optimise meal composition by balancing carbohydrates with protein and healthy fats.
* Engage in regular physical activity, including post-meal walking.
* Promote personalised nutrition interventions tailored to individual risk profiles.

---

## Technologies Used

### Programming Language

* Python

### Development Environment

* Visual Studio Code

### Data Manipulation

* Pandas
* NumPy

### Data Visualisation

* Matplotlib
* Seaborn

### Statistical Analysis

* SciPy

### Machine Learning

* Scikit-learn
* XGBoost

### Explainable AI

* SHAP

### Version Control

* Git
* GitHub

### Deployment

* Streamlit

---

## Repository Structure

```text
nutriglyc-ai-app/
│
├── app.py
├── requirements.txt
├── README.md
├── best_model.pkl
├── model_columns.pkl
│
├── src/
│   └── glucose_spike.py
│
├── outputs/
│   ├── model_comparison_results.csv
│   ├── feature_importance.csv
│   └── shap_outputs/
│
└── data/
```

---

## Future Improvements

Future iterations of this project may incorporate:

* Continuous Glucose Monitoring (CGM) data.
* Wearable device integration.
* Longitudinal patient records.
* Deep learning approaches for sequential glucose prediction.
* External validation using independent populations.
* Real-time personalised nutrition recommendation systems.
---

## Author

**Godswill Okoroafor Chukwu**

MSc Big Data and Data Science Technology (Distinction)

Data Scientist | Healthcare Analytics Enthusiast | STEM Ambassador

GitHub: https://github.com/Godswill-code


