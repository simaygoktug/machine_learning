#Model Dağıtımı ve Üretim Ortamı: Flask ile API ve Docker Kullanımı
#Flask, bir web çerçevesidir ve eğitimden geçirilmiş bir modeli bir API aracılığıyla kullanıma sunmanıza olanak tanır. 

#Pratik Çalışma:

#Flask API oluşturma:

pip install flask numpy scikit-learn

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Veri yükleme
iris = load_iris()
X, y = iris.data, iris.target

# Model eğitimi
model = RandomForestClassifier()
model.fit(X, y)

# Modeli kaydetme
joblib.dump(model, 'iris_model.pkl')
print("Model kaydedildi!")

from flask import Flask, request, jsonify
import joblib
import numpy as np

# Flask uygulaması
app = Flask(__name__)

# Eğitilmiş modeli yükleme
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # JSON formatında gelen veriyi al
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    
    # Tahmin yap
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)

#Docker ile API çalıştırma:

# Python temel imajı
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .
COPY app.py .
COPY iris_model.pkl .

# Gerekli kütüphaneleri yükle
RUN pip install -r requirements.txt

# Uygulamayı başlat
CMD ["python", "app.py"]

#Terminalde şu komutları çalıştırın
docker build -t flask-ml-api .

#Docker konteynerini başlatmak için şu komutu kullanın
docker run -p 5000:5000 flask-ml-api

#API’yi test etme
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'

#Beklenen çıktı
{"prediction": 0}
