import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('healthcare.sav', 'rb'))

st.title('Prediction Cardio Vascular')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Usia')

with col2:
    sex = st.number_input('Jenis Kelamin')

with col3:
    cp = st.number_input('Jenis Nyeri Dada')

with col1:
    trestbps = st.number_input('Tekanan Darah')

with col2:
    chol = st.number_input('Kolestrol')

with col3:
    fbs = st.number_input('Gula Darah > 120 mg/dl')

with col1:
    restecg = st.number_input('Hasil Elektrokardiografi')

with col2:
    thalach = st.number_input('Detak Jantung')

with col3:
    exang = st.number_input('Induksi Angina')

with col1:
    oldpeak = st.number_input('Depresi ST')

with col2:
    slope = st.number_input('Kemiringan Segmen ST')

with col3:
    ca = st.number_input('Jumlah Pembuluh Darah Besar Fluoroskopi')

with col1:
    thal = st.number_input('Tingkat Thal')
    

healthcare_diagnosis = ''

if st.button('Prediction Cardio Vascular'):
    healthcare_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if(healthcare_prediction[0]==1):
        healthcare_diagnosis = 'Pasien Terkena Cardio Vascular'
    else:
        healthcare_diagnosis = 'Pasien Tidak terkena Cardio Vascular'

st.success(healthcare_diagnosis)




