# Employee Salary Prediction App 
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

# --- Load model and encoders ---
model = joblib.load("best_model.pkl")

feature_cols = [
    'age', 'workclass', 'fnlwgt', 'educational-num', 'marital-status', 'occupation',
    'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country'
]

workclass_classes = np.array(['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked', 'Others'])
marital_status_classes = np.array(['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent'])
occupation_classes = np.array(['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces', 'Others'])
relationship_classes = np.array(['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
race_classes = np.array(['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
gender_classes = np.array(['Male', 'Female'])
native_country_classes = np.array([
    'United-States', 'India', 'Canada', 'England', 'Germany', 'Others'
])

def encode_column(val, classes):
    le = LabelEncoder(); le.classes_ = classes; return le.transform([val])[0]

st.set_page_config(page_title="Employee Salary Prediction", page_icon="💼", layout="centered")
st.markdown("""
    <div style='background-color:#eaf2fb; padding: 18px 24px; border-radius: 8px; margin-bottom: 18px;'>
        <h2 style='color:#2b3a55; margin-bottom:8px;'>💼 Employee Salary Prediction</h2>
        <p style='color:#444; font-size:1.05rem; margin-bottom:0;'>
            Enter employee details below to estimate if the annual salary is above or below 50K.
        </p>
    </div>
""", unsafe_allow_html=True)


st.markdown("### 👤 Employee Details")
with st.form("salary_form"):
    age = st.number_input("Age (years)", 17, 90, 30)
    workclass = st.selectbox("Workclass (Type of employer)", [
        'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Others'
    ])
    education_map = {
        'HS-grad': 9,
        'Some-college': 10,
        'Bachelors': 13,
        'Masters': 14,
        'Doctorate': 16
    }
    education_label = st.selectbox("Education Level (Highest attained)", list(education_map.keys()))
    education_num = education_map[education_label]
    occupation = st.selectbox("Occupation (Job role)", [
        'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
        'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
        'Protective-serv', 'Others'
    ])
    gender = st.selectbox("Gender", gender_classes)
    hours_per_week = st.number_input("Hours per week (Average)", 1, 100, 40)

    
    fnlwgt = 100000
    marital_status = marital_status_classes[0]
    relationship = relationship_classes[0]
    race = race_classes[0]
    capital_gain = 0
    capital_loss = 0
    native_country = native_country_classes[0]

    submitted = st.form_submit_button("Predict Salary", use_container_width=True)

    if submitted:
        input_dict = {
            'age': age,
            'workclass': encode_column(workclass, workclass_classes),
            'fnlwgt': fnlwgt,
            'educational-num': education_num,
            'marital-status': encode_column(marital_status, marital_status_classes),
            'occupation': encode_column(occupation, occupation_classes),
            'relationship': encode_column(relationship, relationship_classes),
            'race': encode_column(race, race_classes),
            'gender': encode_column(gender, gender_classes),
            'capital-gain': capital_gain,
            'capital-loss': capital_loss,
            'hours-per-week': hours_per_week,
            'native-country': encode_column(native_country, native_country_classes)
        }
        input_df = pd.DataFrame([input_dict], columns=feature_cols)
        try:
            pred = model.predict(input_df)[0]
            if pred == '>50K':
                st.success("✅ Estimated result: The employee's annual salary is likely above 50K.")
            else:
                st.info("ℹ️ Estimated result: The employee's annual salary is likely 50K or below.")
        except Exception as e:
            st.error("Prediction failed. Please check your inputs.")




