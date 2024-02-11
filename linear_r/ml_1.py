#En küçük kareler metodu

#import mglearn

#mglearn.plots.plot_linear_regression_wave()

#from sklearn.linear_model import LinearRegression

#X,y = mglearn.datasets.make_wave(n_samples=60)

#X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42)

#lr = LinearRegression.fit(X_train, y_train)

#print(lr.coef_)
#print(lr.intercept_)

#print(lr.score(X_train, y_train))
#print(lr.score(X_test, y_test))

#Underfitting var --> %67

#Boston'da oturanların suç oranı hakkında dataset

#from sklearn.datasets import load_boston

#boston=load_boston()

#print(boston["DESCR"])

#X,y=mglearn.datasets.load_extended_boston()

import pandas as pd

veri=pd.read_csv("student-mat.csv",sep=";")

veri=veri[["G1","G2","G3","studytime","failures","absences","age"]]

print(veri.head())

veri.rename(columns={"G1":"First_Midterm","G2":"Second_Midterm","G3":"Final","studytime":"Study_Time","failures":"Failures","absences":"Absences","age":"Age"},inplace=True)

print(veri.head())

print(veri.dtypes)

import numpy as np

y=np.array(veri["Final"])

X=np.array(veri.drop("Final",axis=1))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train,y_train)

print(lr.score(X_test,y_test)) #Underfitting
print(lr.score(X_train,y_train)) #Overfitting

yeni_veri=np.array([10,14,3,0,4,16])
lr.predict(yeni_veri)
