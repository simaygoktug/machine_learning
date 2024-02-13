import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

from sklearn.datasets import make_blobs

X,y=make_blobs(100,2,centers=2,cluster_std=1.5)
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="RdBu")

plt.show()

from sklearn.naive_bayes import GaussianNB

prediction=GaussianNB()
prediction.fit(X,y)

rng=np.random.RandomState(0)
X_yeni=[-6,-14]+[14,18]*rng.rand(1000,2)
y_yeni=prediction.predict(X_yeni)

plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="RdBu")
lim=plt.axis()
plt.scatter(X_yeni[:,0],X_yeni[:,1],c=y_yeni,s=20,cmap="RdBu",alpha=0.2)
plt.axis(lim)

plt.show()
