#Hiperparametre ile model parametreleri farklı şeylerdir. Hiper model parametrelerini tahmin etmek için kullanılır.

#Validation (Geçerleme)

from sklearn.datasets import load_iris

iris=load_iris()

X=iris.data
y=iris.target

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier(n_neighbors=1)

model.fit(X,y)

y_model=model.predict(X)

from sklearn.metrics import accuracy_score

accuracy_score(y,y_model)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,train_size=0.2)

model.fit(X_train,y_train)

y_model_2=model.predict(X_test)

accuracy_score(y_test,y_model_2)

#Şimdi Cross Validation yapacaksın.

#Validation Score ve Traning Score büyük veri setleri için ne kadar yakın olursa o kadar overfitting veya underfitting sorunundan kaçınılmış olur. 
