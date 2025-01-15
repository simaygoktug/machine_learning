#Zaman serisi analizi, zamanla değişen verilerdeki kalıpları anlamak ve gelecekteki değerleri tahmin etmek için kullanılır.
#ARIMA (AutoRegressive Integrated Moving Average), trend ve mevsimsellik gibi özellikleri modellemek için yaygın olarak kullanılan bir tekniktir.

pip install pandas matplotlib statsmodels OR pip install prophet

import pandas as pd

# Örnek veri: Ay ve satış sayıları
data = {
    "Month": ["2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06",
              "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12"],
    "Sales": [250, 265, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460]
}
df = pd.DataFrame(data)

# Tarih sütununu zaman serisine çevir
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

print(df)

import matplotlib.pyplot as plt

# Zaman serisini görselleştir
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Sales'], marker='o', linestyle='-')
plt.title("Aylık Satışlar")
plt.xlabel("Ay")
plt.ylabel("Satış")
plt.grid()
plt.show()

from statsmodels.tsa.arima.model import ARIMA

# ARIMA modeli tanımlama
model = ARIMA(df['Sales'], order=(1, 1, 1))  # ARIMA(p, d, q)
model_fit = model.fit()

# Model özetini yazdır
print(model_fit.summary())

# Gelecekteki değerleri tahmin etme
forecast = model_fit.forecast(steps=6)  # 6 ay ileri tahmin
print("Gelecekteki Tahminler:\n", forecast)

# Tahminleri görselleştirme
future_months = pd.date_range(start="2023-01", periods=6, freq='M')
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Sales'], label="Gerçek Veriler", marker='o')
plt.plot(future_months, forecast, label="Tahmin", marker='x', linestyle='--')
plt.title("ARIMA ile Satış Tahmini")
plt.xlabel("Ay")
plt.ylabel("Satış")
plt.legend()
plt.grid()
plt.show()

