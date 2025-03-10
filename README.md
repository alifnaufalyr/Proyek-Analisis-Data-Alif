# Proyek Analisis Data: Bike Sharing Dataset

Proyek ini bertujuan untuk menganalisis tren peminjaman sepeda berdasarkan faktor-faktor seperti musim, cuaca, dan hari kerja. Hasil analisis ini divisualisasikan dalam bentuk grafik dan dashboard interaktif menggunakan Streamlit.

## Struktur Direktori
```
submission/
├───dashboard/
│   └───dashboard.py
├───data/
│   ├───day.csv
├───Proyek_Analisis_Data (1).ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## Cara Menjalankan Proyek

### 1. Menjalankan Notebook
Buka file `Proyek_Analisis_Data (1).ipynb` di Jupyter Notebook atau Google Colab untuk melakukan eksplorasi dan analisis data.

### 2. Menjalankan Dashboard Streamlit
Untuk menjalankan dashboard interaktif:
1. Pastikan Python sudah terinstal.
2. Install dependensi dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan dashboard dengan perintah berikut:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

## Insight Utama
1. Jumlah peminjaman sepeda lebih tinggi pada musim tertentu, terutama musim panas.
2. Cuaca berpengaruh terhadap tren peminjaman sepeda, dengan penurunan jumlah peminjaman saat cuaca buruk.
3. Hari kerja memiliki dampak signifikan terhadap pola peminjaman, dengan lebih banyak peminjaman pada hari kerja dibandingkan akhir pekan.

## Teknologi yang Digunakan
- **Python** (pandas, seaborn, matplotlib)
- **Jupyter Notebook / Google Colab**
- **Streamlit** (untuk visualisasi interaktif)
