import pandas as pd

df=pd.read_csv("heart.csv")

#df.head()
#DEATH 1 ve 0'lardan oluşan makine öğrenmesine uygun target değişkenimiz. Diğerleri öz nitelikler.
#df.shape()

data=df.sample(frac=0.95,random_state=0)
data_unseen=df.drop(data.index)
#Kalan %5'lik kesim data_unseen değişkenine atandı.

data.reset_İndex(inplace=True,drop=True)
#Şimdi index'ler düzenli 0 'dan başlayarak tekrar oluşturuldu.

data.reset_İndex(inplace=True,drop=True)
#Şimdi index'ler düzenli 0 'dan başlayarak tekrar oluşturuldu.

#data["DEATH"].value_counts()
#Kaç tane 0 kaç tane 1 var görmüş olduk.

from pycaret.classification import *
#Sınıflandırma yapacağız!
from imblearn.over_sampling import RandomOverSampler

model=setup(data=data,
            target="DEATH",
            normalize=True,
            normalize_method="minmax",
            train_size=0.8,
            fix_imbalance=True,
            fix_imbalance_method=RandomOverSampler,
            session_id=0)

#session_id aslında sckitlearn içindeki random_state argümanı ile aynı işlevi görmektedir.

#K-En Yakın Komşu algoritmasını kullanacağız.
knn=create_model("knn")
#Parametre ayarı
tuned_knn=tune_model=(knn)

plot_model(tuned_knn,plot="auc")
plot_model(tuned_knn,plot="pr")
#Model çok iyi değilmiş.

predict_model(tuned_knn)

#Kütüphanedeki bütün algoritmaları test etti.
best=compare_models()
#Parametre ayarı
tuned_best=tune_model(best)

plot_model(tuned_best,plot="pr")
#Bu sefer iyi sonuç verdi.

final_best=finalize_model(tuned_best)
#Final model kuruldu.

predict_model(final_best)
#Accuracy 0.35 yükseldi.

predict_model(final_best,data=data_unseen)
#%60 başarılı oldu.
