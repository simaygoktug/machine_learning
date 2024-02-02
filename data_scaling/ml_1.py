#Sonuçlar bu sefer bilinmiyor.
#Verilerin etiketleri yoktur.

#Blog yazılarını gruplamak için.

#Özniteliklere indirgenir.

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,random_state=1)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
scaler.fit(X_train)

X_train_scaled=scaler.transform(X_train)

X_train.min(axis=0)
X_train_scaled.min(axis=0)

X_train.max(axis=0)
X_train_scaled.max(axis=0)

#Veriler 0 ile 1 arasına sıkıştırıldı.

X_test_scaled=scaler.transform(X_test)
