pip install numpy pandas matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Örnek veri
X_train = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 8]])
y_train = np.array([0, 0, 0, 1, 1, 1])  # 0: Sınıf 1, 1: Sınıf 2

# Yeni veri noktası
X_new = np.array([5, 5])

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def knn_predict(X_train, y_train, X_new, k):
    # Mesafeleri hesapla
    distances = [euclidean_distance(x, X_new) for x in X_train]
    
    # En yakın k komşuyu bul
    k_indices = np.argsort(distances)[:k]
    k_nearest_labels = y_train[k_indices]
    
    # Sınıf oylaması (sınıflandırma için)
    most_common = np.bincount(k_nearest_labels).argmax()
    return most_common

# Tahmin yap
k = 3
prediction = knn_predict(X_train, y_train, X_new, k)
print(f"{X_new} noktası için tahmin edilen sınıf: {prediction}")

# Eğitim verisini ve yeni noktayı görselleştir
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', label="Eğitim Verisi")
plt.scatter(X_new[0], X_new[1], color='green', label="Yeni Nokta")
plt.title("KNN Tahmini")
plt.legend()
plt.grid()
plt.show()
