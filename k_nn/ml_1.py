#Supervised Learning 
#Classification

import mglearn
import numpy as np
import pandas as pd
import matplotlib as plt

#mglearn.plots.plot_knn_classification(n_neighbors=1)
#mglearn.plots.plot_knn_classification(n_neighbors=3)

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

from sklearn.model_selection import train_test_split

X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.neighbors import KNeighborsClassifier

snf = KNeighborsClassifier(n_neighbors = 3)
snf.fit(X_train, y_train)

snf.predict(X_test)

snf.score(X_test,y_test)
#%86 başarı oranı
