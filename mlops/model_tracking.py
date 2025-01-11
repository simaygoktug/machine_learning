#Model izleme, üretimde çalışan bir makine öğrenmesi modelinin performansını, kullanım oranını ve diğer önemli metriklerini sürekli olarak takip etme sürecidir. 
#Model tahminlerinin doğruluğunu kontrol etme ve veri dağılımındaki kaymaları (data drift) tespit etmek için kullanılır.

#Prometheus: Verileri toplar ve zaman serisi bazında saklar.
#Grafana: Prometheus'tan alınan verileri görselleştirir ve kullanıcı dostu bir arayüzde gösterir.

pip install prometheus-client

from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metrikleri
prediction_counter = Counter('prediction_requests', 'Number of prediction requests')
error_counter = Counter('errors', 'Number of errors encountered')

# Basit model (örnek)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        prediction_counter.inc()  # Tahmin isteğini artır
        data = request.get_json()
        # Örnek tahmin (dummy model)
        result = {"prediction": len(data['features'])}
        return jsonify(result)
    except Exception as e:
        error_counter.inc()  # Hata sayısını artır
        return jsonify({"error": str(e)}), 500

# Prometheus metrik endpoint'i
@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'flask_api'
    static_configs:
      - targets: ['localhost:5000']

docker run -d --name=prometheus -p 9090:9090 \
    -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

docker run -d --name=grafana -p 3000:3000 grafana/grafana

curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"features": [1, 2, 3]}'

http://localhost:9090
