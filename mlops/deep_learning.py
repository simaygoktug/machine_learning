#Derin öğrenme çerçeveleri (TensorFlow ve PyTorch), makine öğrenmesi ve derin öğrenme modelleri geliştirmek için güçlü araçlar sunar. 
#TensorFlow, endüstride yaygın kullanılan bir kütüphane olup eğitim, optimizasyon, ve dağıtım için geniş bir ekosistem sunar.

pip install tensorflow

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Veri setini yükle
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Veriyi normalize et
X_train = X_train / 255.0
X_test = X_test / 255.0

# Etiketleri kategorik formata çevir
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Modeli oluştur
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Giriş verisini düzleştir
    Dense(128, activation='relu'),  # Gizli katman
    Dense(10, activation='softmax') # Çıkış katmanı
])

# Modeli derle
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Modeli eğit
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Test verisi üzerinde değerlendirme
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Doğruluğu: {test_acc:.2f}")

import numpy as np

# Bir test görüntüsünü tahmin etme
index = 0
prediction = model.predict(X_test[index].reshape(1, 28, 28))
print(f"Tahmin Edilen: {np.argmax(prediction)}, Gerçek: {np.argmax(y_test[index])}")
