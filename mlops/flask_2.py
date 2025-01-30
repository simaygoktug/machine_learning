pip install flask numpy scikit-learn joblib

#Model Eğitimi ve Kaydetme (Sadece örnek için hiperparametre ayarı yapılmamıştır.)

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Veri setini yükle
iris = load_iris()
X, y = iris.data, iris.target

# Modeli eğit
model = RandomForestClassifier()
model.fit(X, y)

# Modeli kaydet
joblib.dump(model, 'iris_model.pkl')
print("Model başarıyla kaydedildi!")

#Flask API Oluşturma

from flask import Flask, request, jsonify
import joblib
import numpy as np

# Flask uygulaması
app = Flask(__name__)

# Eğitilmiş modeli yükle
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Gelen JSON verisini al
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        
        # Model tahmini yap
        prediction = model.predict(features)
        response = {'prediction': int(prediction[0])}
    except Exception as e:
        response = {'error': str(e)}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

#Docker ile API Dağıtımı

# Python temel imajı
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt .
COPY app.py .
COPY iris_model.pkl .

# Gerekli kütüphaneleri yükle
RUN pip install -r requirements.txt

# Uygulamayı başlat
CMD ["python", "app.py"]

docker build -t flask-ml-api .

docker run -p 5000:5000 flask-ml-api

#API Test Etme

# cURL ile test
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Beklenen çıktı
{"prediction": 0}

# Postman ile test
URL: http://127.0.0.1:5000/predict
Method: POST
Body (JSON):
{
    "features": [5.1, 3.5, 1.4, 0.2]
}

#Metrik İzleme için Prometheus Entegrasyonu

pip install prometheus-client

from prometheus_client import Counter, generate_latest

# Prometheus metrikleri
prediction_counter = Counter('prediction_requests', 'Number of prediction requests')
error_counter = Counter('errors', 'Number of errors encountered')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        prediction_counter.inc()  # Tahmin isteği sayısını artır
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        error_counter.inc()  # Hata sayısını artır
        return jsonify({'error': str(e)})

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200

#Grafana ile İzleme

docker run -d --name=prometheus -p 9090:9090 prom/prometheus
docker run -d --name=grafana -p 3000:3000 grafana/grafana

#Prometheus için bir prometheus.yml dosyası oluşturun.
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'flask_api'
    static_configs:
      - targets: ['host.docker.internal:5000']

#Prometheus'u bu konfigürasyonla çalıştırarak Flask API metriklerini takip edebilirsiniz.