import streamlit as st
import pandas as pd
import joblib

model = joblib.load('KNN_heart.pkl')
scaler =  joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title('Heart Disease Prediction')

st.markdown('Please enter the following details to predict the likelihood of heart disease:')

age = st.slider('Age', 18, 100, 40)

sex = st.selectbox('SEX',['M', 'F'])
chest_pain = st.selectbox('Chest pain type', ['ATA','NAP','TA','ASY'])
resting_blood_pressure = st.number_input('Resting blood pressure', 80, 200, 120)
cholesterol = st.number_input('cholesterol(mg/dl)', 100, 600, 200)
fasting_bs = st.selectbox('Fasting blood sugar > 120 mg/dl', ['0', '1'])
resting_ecg = st.selectbox('Resting electrocardiographic results', ['Normal', 'ST', 'LVH'])
max_hr = st.slider('max heart rate',60,220,150)
excercise_agina = st.selectbox('Excercise induced angina', ['Y', 'N'])
oldspeak = st.slider('oldspeak (ST Depression)', 0.0,6.0,1.0)
st_slope = st.selectbox('ST slope', ['Up', 'Flat', 'Down'])




if st.button('predict'):
    raw_input = {
        'Age': age,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingBP': resting_blood_pressure,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG_' + resting_ecg: 1,
        'MaxHR': max_hr,
        'ExerciseAngina_' + excercise_agina: 1,
        'Oldpeak': oldspeak,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error('⚠️ High Risk of Heart Disease')
    else:
        st.success('✅ Low Risk of Heart Disease')