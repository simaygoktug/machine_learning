#Şahin
#Devekuşu
#Yunus
#Ayı

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,stratify=cancer.target)

from sklearn.tree import DecisionTreeClassifier

#tree=DecisionTreeClassifier()

#tree.fit(X_train,y_train)

#print(tree.score(X_train,y_train)) #1.0
#print(tree.score(X_test,y_test)) #0.91


tree=DecisionTreeClassifier(max_depth=4)

tree.fit(X_train,y_train)

print(tree.score(X_train,y_train)) 
print(tree.score(X_test,y_test)) 

from sklearn.datasets import load_iris

iris=load_iris()

X=iris.data[:,2:]
y=iris.target

tree=DecisionTreeClassifier(max_depth=2)

tree.fit(X,y)

from sklearn.tree import export_graphviz
from sklearn import tree

export_graphviz(tree,out_file="C:\Users\simay\OneDrive\Masaüstü\Yazılım\Makine Öğrenmesi\Karar Ağaçları Algoritması\tree.dot",feature_names=iris.feature_names[2:],class_names=True,filled=True)
