from sklearn.datasets import load_iris

iris=load_iris()
X,y=iris.data,iris.target

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

#X.shape
#150,4

from sklearn.linear_model import LogisticRegression

logreg=LogisticRegression(solver="lbfgs",multi_class="auto",max_iter=1000)
logreg.fit(X_train,y_train)
#%97 başarılı

from sklearn.model_selection import cross_val_score

scores=cross_val_score(logreg,X,y,cv=5)
#5 adet fold oluşturacak.
scores.mean()

#Train-test fonksiyonu rastgele parçalama yapıyor.
#Cross validation ile daha kesin sonuç elde ederiz.
#Ama daha çok zaman alır.

import mglearn

mglearn.plots.plot_stratified_cross_validation()

from sklearn.model_selection import KFold

kfold=KFold(n_splits=3,shuffle=True,random_state=0)
cross_val_score(logreg,iris.data,iris.target,cv="kfold")

#Validation Score ve Traning Score büyük veri setleri için ne kadar yakın olursa o kadar overfitting veya underfitting sorunundan kaçınılmış olur. 
