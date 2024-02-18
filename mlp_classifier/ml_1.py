from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

X,y=make_moons(n_samples=100,noise=0.25,random_state=3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,random_state=42)

mlp=MLPClassifier(max_iter=10000,random_state=0).fit(X_train,y_train)

#Alfa=1, hidden_layer[10,10] --> En regüler modeli oluşturur.

#Böyle verilerde pek optimal çalışmadığı için düzenleme yapacağız.

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(X_train)
scaler.fit(X_test)
X_train_scaled=scaler.transform(X_train)
X_test_scaled=scaler.transform(X_test)

mlp_new=MLPClassifier(max_iter=10000,random_state=42)
mlp_new.fit(X_train_scaled,y_train)

#Alfa=1, hidden_layer[10,10] --> En regüler modeli oluşturur.
