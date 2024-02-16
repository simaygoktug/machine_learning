#Regülasyon

#Model çok fazla öznitelik olduğu için ezberlemeye girecek ve overfitting ortaya çıkacak.

#Ridge Regresyon

from sklearn.datasets import load_boston
 
boston=load_boston()

print(boston["DESCR"])

import mglearn

X,y = mglearn.datasets.load_extended_boston()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

from sklearn.linear_model import Ridge

ridge=Ridge().fit(X_train,y_train)

ridge10=Ridge(alpha=10).fit(X_train,y_train)

#0.1 de deneyebilirsin.

#Lasso da aynı syntax ile denenir.

#Ama alfayı çok düşürmen ve 0.01 yapman gerekir. max_iter=100000 yapmayı da unutma!
