import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('model/model.joblib')

st.title("🎓 Prediksi Status Mahasiswa")

st.markdown("Masukkan data mahasiswa untuk memprediksi apakah mereka akan **Graduate**, **Dropout**, atau masih **Enrolled**.")

# Input dari user
age = st.slider("Umur saat masuk (Age at Enrollment)", 17, 70, 20)
admission_grade = st.slider("Admission Grade", 0.0, 200.0, 120.0)
curricular_units_1st_sem_grade = st.slider("Nilai Semester 1", 0.0, 20.0, 10.0)
curricular_units_2nd_sem_grade = st.slider("Nilai Semester 2", 0.0, 20.0, 10.0)
curricular_units_1st_sem_approved = st.number_input("Jumlah Unit Lulus Semester 1", 0, 10, 5)
curricular_units_2nd_sem_approved = st.number_input("Jumlah Unit Lulus Semester 2", 0, 10, 5)

# Biner
debtor = st.selectbox("Status Debtor", ['No', 'Yes'])
tuition_up_to_date = st.selectbox("Biaya Kuliah Terbayar", ['Yes', 'No'])
scholarship = st.selectbox("Penerima Beasiswa", ['No', 'Yes'])
gender = st.selectbox("Gender", ['Female', 'Male'])

# Mapping input ke numerik
binary_map = {'No': 0, 'Yes': 1}
gender_map = {'Female': 0, 'Male': 1}

input_data = np.array([[
    age,
    admission_grade,
    curricular_units_1st_sem_grade,
    curricular_units_2nd_sem_grade,
    curricular_units_1st_sem_approved,
    curricular_units_2nd_sem_approved,
    binary_map[debtor],
    binary_map[tuition_up_to_date],
    binary_map[scholarship],
    gender_map[gender]
]])

if st.button("Prediksi"):
    pred = model.predict(input_data)[0]
    label_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
    st.success(f"📊 Prediksi Status Mahasiswa: **{label_map[pred]}**")
