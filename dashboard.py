import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('day.csv')  # Sesuaikan dengan dataset yang digunakan

# Title
st.title("Bike Sharing Dashboard")

# Sidebar filters
# Mapping kategori musim dan hari kerja
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df['season'] = df['season'].map(season_map)

day_type_map = {0: "Libur", 1: "Hari Kerja"}
df['workingday'] = df['workingday'].map(day_type_map)

# Sidebar image
st.sidebar.image("weather.png", caption="Weather Conditions", width=200)

# Perubahan Filter dari Radio Button ke Select Box
season_options = ['All Season'] + list(df['season'].unique())
selected_season = st.sidebar.selectbox("Pilih Musim:", season_options)

workingday_options = ['Work Days or Holiday'] + list(df['workingday'].unique())
selected_workingday = st.sidebar.selectbox("Pilih Hari Kerja:", workingday_options)

# Filter data
if selected_season != 'All Season':
    df = df[df['season'] == selected_season]
if selected_workingday != 'Work Days or Holiday':
    df = df[df['workingday'] == selected_workingday]

# Visualisasi jumlah peminjaman sepeda berdasarkan musim
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df['cnt'], bins=30, kde=True, color='blue', ax=ax)
ax.set_xlabel("Jumlah Peminjaman Sepeda")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Visualisasi jumlah peminjaman berdasarkan musim dan hari kerja dengan Line Chart
df_grouped_season = df.groupby('season')['cnt'].mean().reset_index()

df_grouped_workingday = df.groupby('workingday')['cnt'].mean().reset_index()

st.subheader("Tren Peminjaman Sepeda Berdasarkan Musim dan Hari Kerja")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df_grouped_season['season'], df_grouped_season['cnt'], marker='o', linestyle='-', color='b', label='Rata-rata Peminjaman')
ax.axhline(df['cnt'].mean(), color='r', linestyle='--', label='Rata-rata Keseluruhan')
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Peminjaman Sepeda Berdasarkan Musim")
ax.legend()
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df_grouped_workingday['workingday'], df_grouped_workingday['cnt'], marker='o', linestyle='-', color='g', label='Rata-rata Peminjaman')
ax.axhline(df['cnt'].mean(), color='r', linestyle='--', label='Rata-rata Keseluruhan')
ax.set_xlabel("Hari Kerja")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Peminjaman Sepeda pada Hari Kerja vs Hari Libur")
ax.legend()
st.pyplot(fig)

# Visualisasi rata-rata peminjaman sepeda berdasarkan musim
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
df_season = df.groupby('season')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=df_season['season'], y=df_season['cnt'], palette='coolwarm', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Visualisasi rata-rata peminjaman sepeda berdasarkan cuaca
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
df_weather = df.groupby('weathersit')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=df_weather['weathersit'], y=df_weather['cnt'], palette='viridis', ax=ax)
ax.set_xlabel("Cuaca (1: Cerah, 2: Berawan, 3: Hujan, 4: Cuaca Ekstrem)")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Deskripsi Grafik
st.write("""
### Deskripsi Grafik:
Grafik ini menampilkan rata-rata peminjaman sepeda berdasarkan musim. Musim yang dianalisis meliputi **Spring (Musim Semi), Summer (Musim Panas), Fall (Musim Gugur), dan Winter (Musim Dingin)**. Grafik ini bertujuan untuk memahami bagaimana perubahan musim memengaruhi jumlah peminjaman sepeda.

### Tren Utama:
- **Musim Gugur (Fall):** Peminjaman sepeda tertinggi terjadi pada musim gugur, dengan rata-rata lebih dari 5500 peminjaman.
- **Musim Panas (Summer):** Jumlah peminjaman masih tinggi, tetapi sedikit lebih rendah dibandingkan musim gugur, berada di sekitar 5000 peminjaman.
- **Musim Dingin (Winter):** Rata-rata peminjaman tetap cukup tinggi, meskipun mengalami sedikit penurunan dibandingkan musim gugur dan panas, berkisar sekitar 4500 peminjaman.
- **Musim Semi (Spring):** Musim semi memiliki jumlah peminjaman terendah dibandingkan musim lainnya, dengan rata-rata sekitar 2500 peminjaman.

### Analisis:
- **Musim gugur memiliki tingkat peminjaman tertinggi,** kemungkinan karena suhu yang lebih nyaman untuk bersepeda dibandingkan musim panas yang lebih panas atau musim dingin yang lebih dingin.
- **Musim panas juga memiliki tingkat peminjaman yang tinggi,** kemungkinan didorong oleh kondisi cuaca yang lebih stabil dan liburan musim panas yang meningkatkan aktivitas luar ruangan.
- **Musim dingin tetap memiliki jumlah peminjaman yang relatif tinggi,** meskipun kondisi cuaca lebih dingin. Ini mungkin menunjukkan bahwa ada pengguna yang masih mengandalkan sepeda sebagai transportasi utama.
- **Musim semi menunjukkan jumlah peminjaman yang paling sedikit,** yang bisa disebabkan oleh faktor seperti hujan yang lebih sering atau transisi dari musim dingin yang membuat orang belum terlalu aktif bersepeda.

### Kesimpulan:
Grafik ini menunjukkan bahwa musim memiliki pengaruh signifikan terhadap tingkat peminjaman sepeda. Peminjaman tertinggi terjadi pada musim gugur dan panas, sementara musim semi memiliki peminjaman terendah. Informasi ini dapat digunakan oleh penyedia layanan sepeda untuk mengoptimalkan ketersediaan dan promosi berdasarkan musim, seperti memberikan insentif di musim semi untuk meningkatkan penggunaan atau menyiapkan fasilitas khusus untuk musim dingin.
""")
# Tambahan: Visualisasi rata-rata peminjaman sepeda berdasarkan cuaca
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
df_weather = df.groupby('weathersit')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=df_weather['weathersit'], y=df_weather['cnt'], palette='viridis', ax=ax)
ax.set_xlabel("Cuaca (1: Cerah, 2: Berawan, 3: Hujan, 4: Cuaca Ekstrem)")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
st.pyplot(fig)
# Deskripsi Grafik
st.write("""
### Deskripsi Grafik:
Grafik ini menampilkan rata-rata peminjaman sepeda berdasarkan kondisi cuaca. Cuaca dikategorikan menjadi empat jenis:
1 (Cerah), 2 (Berawan), 3 (Hujan), dan 4 (Cuaca Ekstrem). Namun, dalam grafik ini hanya terlihat tiga kategori cuaca yang memiliki data peminjaman sepeda.

### Tren Utama:
- **Cuaca Cerah (1):** Rata-rata peminjaman sepeda tertinggi terjadi pada kondisi cuaca cerah, dengan jumlah peminjaman mendekati 5000 sepeda.
- **Cuaca Berawan (2):** Jumlah peminjaman sedikit lebih rendah dibandingkan cuaca cerah, sekitar 4000 sepeda, tetapi masih cukup tinggi.
- **Cuaca Hujan (3):** Peminjaman sepeda mengalami penurunan drastis, hanya sekitar 2000 sepeda.
- **Cuaca Ekstrem (4):** Tidak terlihat dalam grafik, kemungkinan tidak ada data atau jumlah peminjaman sangat rendah.

### Analisis:
- Grafik menunjukkan bahwa semakin buruk kondisi cuaca, semakin rendah jumlah peminjaman sepeda.
- Penurunan yang tajam saat hujan menunjukkan bahwa pengguna sepeda cenderung menghindari peminjaman dalam kondisi basah.
- Tidak adanya data untuk cuaca ekstrem bisa berarti sangat sedikit atau bahkan tidak ada peminjaman sama sekali pada kondisi tersebut.

### Kesimpulan:
Grafik ini memberikan wawasan bahwa cuaca berpengaruh signifikan terhadap jumlah peminjaman sepeda. Dalam cuaca cerah dan berawan, jumlah peminjaman tetap tinggi, sedangkan saat hujan, peminjaman menurun drastis. Informasi ini dapat digunakan untuk perencanaan layanan sepeda, seperti penyediaan fasilitas pelindung hujan atau promosi khusus untuk meningkatkan penggunaan sepeda dalam cuaca buruk.
""")

# Kesimpulan
st.subheader("Rangkuman")
st.write("- Jumlah peminjaman sepeda cenderung lebih tinggi di musim tertentu.")
st.write("- Hari kerja memiliki pengaruh terhadap jumlah peminjaman sepeda.")
st.write("- Rata-rata peminjaman sepeda berbeda pada setiap musim, dengan tren tertentu yang dapat diidentifikasi dari data historis.")
st.write("- Cuaca juga mempengaruhi rata-rata peminjaman sepeda, dengan tren yang menunjukkan bahwa kondisi cerah lebih disukai pengguna.")