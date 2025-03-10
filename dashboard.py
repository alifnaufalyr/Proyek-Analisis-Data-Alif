import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('day.csv')  # Sesuaikan dengan dataset yang digunakan

# Title
st.title("Bike Sharing Dashboard")

# Sidebar filters
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df['season'] = df['season'].map(season_map)

day_type_map = {0: "Libur", 1: "Hari Kerja"}
df['workingday'] = df['workingday'].map(day_type_map)

selected_season = st.sidebar.radio("Pilih Musim:", ['Spring', 'Summer', 'Fall', 'Winter'])
selected_workingday = st.sidebar.radio("Pilih Hari Kerja:", ['Hari Kerja', 'Libur'])

# Filter data
filtered_data = df[(df['season'] == selected_season) & (df['workingday'] == selected_workingday)]

# Visualisasi jumlah peminjaman sepeda berdasarkan musim
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_data['cnt'], bins=30, kde=True, color='blue', ax=ax)
ax.set_xlabel("Jumlah Peminjaman Sepeda")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Visualisasi jumlah peminjaman berdasarkan musim dan hari kerja
st.subheader("Tren Peminjaman Sepeda Berdasarkan Musim dan Hari Kerja")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=filtered_data['season'], y=filtered_data['cnt'], palette='coolwarm', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Perbandingan Jumlah Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=filtered_data['workingday'], y=filtered_data['cnt'], palette='viridis', ax=ax)
ax.set_xlabel("Hari Kerja")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Perbandingan Jumlah Peminjaman Sepeda pada Hari Kerja vs Hari Libur")
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("- Jumlah peminjaman sepeda cenderung lebih tinggi di musim tertentu.")
st.write("- Hari kerja memiliki pengaruh terhadap jumlah peminjaman sepeda.")
