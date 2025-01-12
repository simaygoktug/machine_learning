#Veri görselleştirme, veriyi anlamak ve analiz sonuçlarını etkili bir şekilde sunmak için grafikler ve görseller oluşturma sürecidir. 
#Seaborn ve Matplotlib, Python'da güçlü veri görselleştirme kütüphaneleridir.

pip install matplotlib seaborn pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
df = pd.read_csv("sales_data.csv")

# 1. Bar Grafiği: Kategoriye Göre Satışlar
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Sales', data=df, palette='Blues')
plt.title("Kategoriye Göre Toplam Satışlar")
plt.xlabel("Kategori")
plt.ylabel("Satış")
plt.show()

# 2. Bölgeye Göre Kar Dağılımı
plt.figure(figsize=(8, 5))
sns.boxplot(x='Region', y='Profit', data=df, palette='Set3')
plt.title("Bölgeye Göre Kar Dağılımı")
plt.xlabel("Bölge")
plt.ylabel("Kar")
plt.show()

# 3. Satış ve Kar İlişkisi: Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', style='Region', s=100)
plt.title("Satış ve Kar İlişkisi")
plt.xlabel("Satış")
plt.ylabel("Kar")
plt.legend(title="Kategori ve Bölge")
plt.show()
