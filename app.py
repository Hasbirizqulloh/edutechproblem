import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("model/model.joblib")

# Mapping hasil prediksi
reverse_mapping = {0: "❌ Dropout", 1: "📚 Enrolled", 2: "🎓 Graduate"}

# UI Title dan Deskripsi
st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="centered")
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("""
Masukkan informasi akademik dan demografis mahasiswa untuk memprediksi apakah mereka akan:

- ❌ **Dropout**
- 📚 **Enrolled**
- 🎓 **Graduate**
""")

# Layout dengan columns untuk form input
col1, col2 = st.columns(2)

with col1:
    grade_1st = st.number_input("📘 Nilai Semester 1", min_value=0.0, max_value=20.0, value=10.0)
    approved_1st = st.number_input("✅ Jumlah MK Lulus Semester 1", min_value=0, max_value=10, value=4)
    fees_up_to_date = st.selectbox("💵 Uang Kuliah Terbayar?", ("Yes", "No"))
    debtor = st.selectbox("💳 Memiliki Utang Pendidikan?", ("Yes", "No"))
    # Mapping kode ke deskripsi
    application_mode_mapping = {
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93",
        5: "1st phase - special contingent (Azores Island)",
        7: "Holders of other higher courses",
        10: "Ordinance No. 854-B/99",
        15: "International student (bachelor)",
        16: "1st phase - special contingent (Madeira Island)",
        17: "2nd phase - general contingent",
        18: "3rd phase - general contingent",
        26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
        27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
        39: "Over 23 years old",
        42: "Transfer",
        43: "Change of course",
        44: "Technological specialization diploma holders",
        51: "Change of institution/course",
        53: "Short cycle diploma holders",
        57: "Change of institution/course (International)"
    }

    # Balik mapping agar bisa mendapatkan kodenya kembali
    label_to_code = {v: k for k, v in application_mode_mapping.items()}

    # Pilih metode aplikasi dengan label deskriptif
    application_mode_label = st.selectbox(
        "📝 Metode Pendaftaran",
        list(application_mode_mapping.values())
    )
    application_mode = label_to_code[application_mode_label]


with col2:
    grade_2nd = st.number_input("📘 Nilai Semester 2", min_value=0.0, max_value=20.0, value=10.0)
    approved_2nd = st.number_input("✅ Jumlah MK Lulus Semester 2", min_value=0, max_value=10, value=4)
    scholarship = st.selectbox("🎁 Penerima Beasiswa?", ("Yes", "No"))
    gender = st.selectbox("⚧️ Jenis Kelamin", ("Female", "Male"))
    age = st.slider("🎂 Usia Saat Masuk", min_value=17, max_value=70, value=20)

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

# Tombol prediksi
st.markdown("---")
if st.button("🔮 Prediksi Status Mahasiswa"):
    prediction = model.predict(input_data)[0]
    st.success(f"Hasil Prediksi: **{reverse_mapping[prediction]}**")

    # Info tambahan
    st.info("📌 Ini hanya prediksi berbasis data historis, bukan hasil final.")
