#Classification

#C=100.000.000 olursa daha AZ regülasyon yapılmış olur.
#Ancak muhtelemelen overfitting gerçekleşir.

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

print(cancer)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

from sklearn.linear_model import LogisticRegression

prediction=LogisticRegression(solver="liblinear").fit(X_train, y_train)

print(prediction.score(X_train, y_train))
print(prediction.score(X_test, y_test))

prediction_for_C100=LogisticRegression(C=100,solver="liblinear").fit(X_train, y_train)

print(prediction.score(X_train, y_train))
print(prediction.score(X_test, y_test))

#print(X_train.shape())
#print(y_train.shape())
#plt.scatter(cancer.data, cancer.target)
#plt.xlabel("Öznitelik 0")
#plt.ylabel("Öznitelik 1")
#plt.legend(["Sinif 0", "Sinif 1"]) 
#plt.plot(cancer.data, cancer.target)
#plt.subplot(211)
#plt.plot(cancer.data)
#plt.subplot(212)
#plt.plot(cancer.target)
#plt.show() 

#Regülerleşme azaldı ve modelin performansı arttı. (Öznitelik sayısından kısma yapılır.)

#from sklearn.datasets import make_blobs
#import mglearn

#%matplotlib inline

#X, y=make_blobs(random_state=42)

#import matplotlib.pyplot as plt

#mglearn.discrete_scatter(X[:,0], X[:,1], y)

#plt.xlabel("Öznitelik 0")
#ply.ylabel("Öznitelik 1")
#plt.legend(["Sinif 0", "Sinif 1", "Sinif 2"])
