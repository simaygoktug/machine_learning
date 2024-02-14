#Zincirleme Faaliyet

from sklearn.datasets import _samples_generator

X,y=_samples_generator.make_classification(n_features=20,n_informative=3,n_redundant=0,n_classes=4,n_clusters_per_class=2)

#Train-Test split yap. (Her zamanki gibi)

from sklearn.feature_selection import SelectKBest, f_regression

anova_filter=SelectKBest(f,f_regression,k=3)

from sklearn.svm import LinearSVC

clf=LinearSVC()

from sklearn.pipeline import make_pipeline

anova_svm=make_pipeline(anova_filter,clf)

anova_svm.fit(X_train,y_train)

y_pred=anova_svm.predict(X_test)

#Score ile analiz edebilirsin. --> %56 başarı oranı.

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

#Train-Test split yap. (Her zamanki gibi)

from sklearn.svm import SVC

from sklearn.preprocessing import MinMaxScaler

pp=make_pipeline(MinMaxScaler(),SVC(gamma="auto"))

pp.fit(X_train,y_train)
