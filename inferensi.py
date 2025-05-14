import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model dan encoder
model = joblib.load('model/model.joblib')

# Mapping balik label (0, 1, 2) ke nama status
reverse_mapping = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}

st.title("🎓 Prediksi Status Mahasiswa")

st.markdown("""
Masukkan informasi berikut untuk memprediksi apakah mahasiswa akan **Dropout**, **Enrolled**, atau **Graduate**.
""")

# Input fitur dari user
grade_2nd = st.number_input("Nilai semester 2", min_value=0.0, max_value=20.0, value=10.0)
approved_2nd = st.number_input("Jumlah mata kuliah lulus semester 2", min_value=0, max_value=10, value=4)
grade_1st = st.number_input("Nilai semester 1", min_value=0.0, max_value=20.0, value=10.0)
approved_1st = st.number_input("Jumlah mata kuliah lulus semester 1", min_value=0, max_value=10, value=4)
fees_up_to_date = st.selectbox("Uang kuliah terbayar?", ("Yes", "No"))
age = st.slider("Usia saat masuk", min_value=17, max_value=70, value=20)
scholarship = st.selectbox("Penerima beasiswa?", ("Yes", "No"))
debtor = st.selectbox("Memiliki utang pendidikan?", ("Yes", "No"))
gender = st.selectbox("Jenis kelamin", ("Female", "Male"))
application_mode = st.selectbox("Metode Pendaftaran", list(range(1, 20)))  # ganti sesuai unique value sebenarnya

# Konversi input ke format model
input_data = np.array([[
    grade_2nd,
    approved_2nd,
    grade_1st,
    approved_1st,
    1 if fees_up_to_date == "Yes" else 0,
    age,
    1 if scholarship == "Yes" else 0,
    1 if debtor == "Yes" else 0,
    1 if gender == "Male" else 0,
    application_mode
]])

# Prediksi
if st.button("🔮 Prediksi Status"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎓 Prediksi: **{reverse_mapping[prediction]}**")
