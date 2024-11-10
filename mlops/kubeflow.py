#Kubeflow, Kubernetes üzerinde çalışan açık kaynaklı bir MLOps platformudur. 
#Kubernetes'in esnekliğinden faydalanarak ML iş akışlarını ölçeklenebilir ve taşınabilir hale getirir. 
#Kubeflow, eğitimden model dağıtımına kadar olan tüm süreci kapsar ve ML geliştiricileri için ideal bir altyapı sunar.

#Kubeflow'u kurmak için bir Kubernetes kümesine ihtiyacınız var. 
#Bu küme, yerel (minikube, kind) veya bulut tabanlı (AWS EKS, GCP GKE, Azure AKS) olabilir.

#Minikube kurulum rehberi üzerinden gerekli adımları izleyerek Kubernetes’i yerel bilgisayarınıza kurun.
#Kubeflow'u indir ve kur:

minikube start --cpus=4 --memory=8192
curl -LO https://github.com/kubeflow/manifests/archive/refs/tags/v1.4.0.tar.gz
tar -xvzf v1.4.0.tar.gz
cd manifests-1.4.0
./kfctl apply -V -f kfctl_k8s_istio.v1.4.0.yaml

#############################################################################################################

#Kurulum tamamlandıktan sonra minikube’un IP adresini kullanarak Kubeflow arayüzüne erişebilirsiniz:

minikube service istio-ingressgateway -n istio-system --url

#############################################################################################################

#Kubeflow birçok bileşeni içerir ve bunlar ML iş akışlarını otomatikleştirmenize yardımcı olur:
#Kale: Model eğitimi için boru hatları oluşturur.
#Katib: Hiperparametre optimizasyonu yapar.
#KFServing: Modellerin servis olarak dağıtılmasını sağlar.
#Notebooks: Jupyter Notebook sunucularını Kubernetes üzerinde çalıştırmanızı sağlar.

#############################################################################################################

#Boru hatları, bir ML iş akışının tüm adımlarını içerir ve veri ön işleme, eğitim, değerlendirme, dağıtım gibi süreçleri kapsar.
#Örnek Boru Hattı Oluşturma:
#Jupyter Notebook Oluşturma:

pip install kfp

#############################################################################################################

#Pipeline Adımlarını Tanımlama:

import kfp
from kfp import dsl

#Veri ön işleme adımı
def preprocess_op():
    return dsl.ContainerOp(
        name="Veri Ön İşleme",
        image="python:3.8",
        command=["python", "-c"],
        arguments=["print('Veri ön işleme tamamlandı!')"]
    )

#Eğitim adımı
def train_op():
    return dsl.ContainerOp(
        name="Model Eğitimi",
        image="python:3.8",
        command=["python", "-c"],
        arguments=["print('Model eğitimi tamamlandı!')"]
    )

#Pipeline tanımlama
@dsl.pipeline(
    name="Basit ML Pipeline",
    description="Veri ön işleme ve model eğitimi adımlarını içeren basit bir pipeline."
)
def simple_ml_pipeline():
    preprocess = preprocess_op()
    train = train_op().after(preprocess)

# Pipeline'ı çalıştırma
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_ml_pipeline, 'simple_ml_pipeline.yaml')

#############################################################################################################

#Pipeline’ı Yükleme ve Çalıştırma:

python pipeline.py

#############################################################################################################

#Hiperparametre Optimizasyonu (Katib ile):
#Kubeflow’un Katib bileşeni, hiperparametre optimizasyonu için kullanılır. 
#Eğitim sürecinde çeşitli hiperparametre kombinasyonlarını test eder ve en iyi performansı veren modeli bulur.

apiVersion: "kubeflow.org/v1beta1"
kind: Experiment
metadata:
  name: example-experiment
  namespace: kubeflow
spec:
  objective:
    type: maximize
    goal: 0.99
    objectiveMetricName: accuracy
  algorithm:
    algorithmName: random
  parameters:
    - name: learning_rate
      parameterType: double
      feasibleSpace:
        min: "0.01"
        max: "0.1"
    - name: batch_size
      parameterType: int
      feasibleSpace:
        min: "16"
        max: "64"

#############################################################################################################

#Kubectl ile Deneyi Çalıştırma:

kubectl apply -f example-experiment.yaml

#############################################################################################################

#Model Dağıtımı (KFServing ile): Eğitilmiş modellerin Kubernetes üzerinde API hizmeti olarak sunulmasını sağlar.
#Model Servis Tanımlama Dosyası:

apiVersion: "serving.kubeflow.org/v1beta1"
kind: "InferenceService"
metadata:
  name: mnist-sample
  namespace: kubeflow
spec:
  predictor:
    tensorflow:
      storageUri: "gs://your-bucket/mnist-model"

#############################################################################################################

#Kubectl ile Model Servisini Başlatma:

kubectl apply -f mnist-sample.yaml

#############################################################################################################

#Servis Adresine Erişim: Modellerinizi REST API olarak kullanabilirsiniz.

curl -d '{"instances": [[...]]}' -H "Content-Type: application/json" -X POST http://<service-ip>/v1/models/mnist-sample:predict

#############################################################################################################

#Sonuç: 

#Bu Kubeflow rehberiyle, Kubeflow’un kurulumu, boru hatları oluşturma, hiperparametre optimizasyonu ve model dağıtımı konularında temel bir anlayış kazandınız. 
#Kubeflow, ML projelerinizin uçtan uca otomatikleştirilmesi, ölçeklenmesi ve yönetilmesi için güçlü bir araçtır. 
#Kubernetes’in sunduğu esnekliğin üzerine inşa edilmiş olması, projelerinizi bulut veya yerel ortamlarda sorunsuz bir şekilde yönetmenizi sağlar.