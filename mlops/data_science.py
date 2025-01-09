#Veri mühendisliği, veri biliminde ham veriyi analiz edilebilir ve model için uygun hale getirme sürecidir. 
#Bu süreç genellikle şu adımları içerir:

#Veri Kazıma (Scraping): Web veya diğer kaynaklardan veri alma.
#Veri Temizleme: Eksik veya hatalı verileri düzeltme.
#Veri Dönüştürme: Veriyi analiz veya modelleme için uygun formata getirme.

#Pratik Örnek:

import pandas as pd

# Veri setini yükle
df = pd.read_csv("sales_data.csv")

# 1. Eksik Verileri İnceleme
print("Eksik Veriler:\n", df.isnull().sum())

# 2. Eksik Verileri Doldurma
df['Price'].fillna(df['Price'].mean(), inplace=True)  # Fiyat eksikse ortalama ile doldur
df['Quantity'].fillna(1, inplace=True)  # Eksik miktarları 1 ile doldur
df['Date'].fillna("2023-01-01", inplace=True)  # Eksik tarihleri varsayılan bir tarihle doldur

# 3. Yeni Bir Sütun Ekleyerek Toplam Satış Hesaplama
df['Total'] = df['Price'] * df['Quantity']

# 4. Tarih Sütununu Tarih Tipine Çevirme
df['Date'] = pd.to_datetime(df['Date'])

# 5. Veriyi Gruplayarak Toplam Geliri Hesaplama
total_revenue = df.groupby('Customer')['Total'].sum()

# Sonuçları Yazdır
print("\nTemizlenmiş Veri:\n", df)
print("\nMüşteri Bazında Toplam Gelir:\n", total_revenue)
