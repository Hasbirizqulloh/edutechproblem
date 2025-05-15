# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang berfokus pada peningkatan kualitas akademik dan pengelolaan mahasiswa secara efisien. Dalam menghadapi tantangan tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout), institusi perlu melakukan pendekatan berbasis data untuk memahami pola-pola performa mahasiswa serta faktor-faktor sosial, ekonomi, dan akademik yang memengaruhi keberhasilan studi.
Manajemen institusi menginginkan adanya alat bantu visualisasi yang interaktif untuk memantau performa mahasiswa secara menyeluruh dan membantu pengambilan keputusan berbasis bukti (evidence-based decision making).

### Permasalahan Bisnis
Beberapa tantangan utama yang dihadapi oleh pihak institusi antara lain:
1. Tingginya angka mahasiswa dropout yang belum diketahui penyebab pastinya.
2. Kesulitan dalam memantau performa akademik mahasiswa secara kolektif, khususnya berdasarkan program studi, gender, dan status beasiswa.
3. Kebutuhan untuk menganalisis korelasi antar variabel akademik dan sosial sebagai indikator potensi risiko dropout.
4. Kurangnya alat visualisasi interaktif yang bisa digunakan oleh pihak manajemen tanpa perlu keahlian teknis.

### Cakupan Proyek
Proyek ini akan mencakup hal-hal berikut:
1. Pembangunan dashboard visualisasi interaktif berbasis Streamlit untuk menganalisis performa dan status mahasiswa.
2. Penerapan filtering dinamis untuk segmentasi data berdasarkan gender, program studi, dan status mahasiswa.
3. Visualisasi distribusi dan tren performa akademik, termasuk rata-rata nilai per semester.
4. Analisis faktor risiko dropout seperti status hutang, kepemilikan beasiswa, dan keterlambatan pembayaran biaya kuliah.
5. Rekomendasi awal berbasis data untuk membantu tim akademik dalam mengambil langkah preventif terhadap potensi dropout.

### Persiapan

Sumber data: Dataset yang digunakan berasal dari repository github [Dicoding](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) dan dataset ini berisi informasi demografis, akademik, serta faktor sosial-ekonomi mahasiswa. Dataset ini umum digunakan untuk analisis performa mahasiswa dan prediksi risiko dropout, dan cocok sebagai dasar pengembangan sistem monitoring untuk institusi pendidikan tinggi. Setup environment:

Setup environment:
```
python -m venv env  
# Aktifkan environment:  
# Windows: .\env\Scripts\activate  
# MacOS/Linux: source env/bin/activate  
pip install -r requirements.txt
streamlit run dashboard.py
```

## Business Dashboard
Dashboard yang telah dibuat berfungsi sebagai alat bantu visualisasi untuk memantau performa mahasiswa secara menyeluruh di sebuah institusi pendidikan tinggi. Dashboard ini menampilkan berbagai metrik dan grafik interaktif berdasarkan data akademik, demografi, dan sosial ekonomi mahasiswa, sehingga memudahkan pihak manajemen atau dosen wali dalam:
1. Mengidentifikasi status akademik mahasiswa (aktif, lulus, dropout)
2. Menganalisis distribusi performa berdasarkan program studi, jenis kelamin, dan status sosial
3. Melihat rata-rata nilai semester berdasarkan status
4. Mengevaluasi faktor risiko yang berhubungan dengan dropout seperti penerima beasiswa, keterlambatan pembayaran UKT, dan status hutang

Dashboard dibuat menggunakan Streamlit dan dapat diakses secara lokal dan secara online melalui platform Streamlit Cloud.

🔗 Link Dashboard : [klik disini](https://dashboardedutech.streamlit.app/)

## Menjalankan Sistem Machine Learning
Sistem machine learning yang dikembangkan bertujuan untuk memprediksi status akhir mahasiswa berdasarkan beberapa fitur akademik dan demografis seperti nilai, jumlah mata kuliah lulus, status pembayaran UKT, status beasiswa, dan lain-lain. Sistem ini dapat memprediksi apakah mahasiswa kemungkinan besar akan Dropout, tetap Enrolled, atau berhasil Graduate.

Prototype sistem dibuat dalam bentuk aplikasi interaktif menggunakan Streamlit, sehingga pengguna tanpa latar belakang teknis tetap dapat mengakses dan menggunakan model prediksi dengan mudah.

```
python -m venv env  
# Aktifkan environment:  
# Windows: .\env\Scripts\activate  
# MacOS/Linux: source env/bin/activate  
pip install -r requirements.txt
streamlit run app.py
```

🚀 Link Prototype : [Klik Disini](https://edutechproblem-nsfc9yjgpus4xeuznyzttx.streamlit.app/)

## Conclusion
Proyek ini berhasil mengembangkan dashboard interaktif dan prototype sistem machine learning untuk memantau serta memprediksi performa akademik mahasiswa. Berdasarkan data historis, dashboard mampu memberikan wawasan visual yang jelas terkait distribusi status mahasiswa, rata-rata nilai, hingga faktor-faktor risiko dropout seperti status pembayaran UKT, penerima beasiswa, dan hutang pendidikan.

Sementara itu, sistem prediksi berbasis machine learning telah dibangun untuk memberikan estimasi status mahasiswa di masa depan (Dropout, Enrolled, atau Graduate) berdasarkan input fitur tertentu. Sistem ini dapat membantu institusi pendidikan dalam mengambil keputusan berbasis data yang lebih proaktif untuk meningkatkan tingkat kelulusan dan mengurangi angka putus studi.

### Rekomendasi Action Items
Berikut beberapa rekomendasi langkah konkret yang dapat dilakukan oleh pihak institusi:

- Meningkatkan monitoring terhadap mahasiswa dengan risiko tinggi seperti mereka yang tidak melunasi UKT tepat waktu, memiliki beban hutang pendidikan, atau memiliki nilai rendah di semester awal.

- Mengembangkan program intervensi akademik dan sosial, misalnya: kelas remedial, dukungan konseling, atau bantuan keuangan tambahan bagi mahasiswa berisiko dropout.

- Mengintegrasikan sistem prediksi ke sistem akademik internal, sehingga staf akademik dan dosen pembimbing dapat langsung melihat prediksi risiko dan segera menindaklanjuti.

- Melakukan evaluasi berkala terhadap model prediksi, agar tetap relevan dan akurat sesuai dengan kondisi terbaru mahasiswa dan kurikulum.
