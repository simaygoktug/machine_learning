#Lineer DVM

from sklearn.datasets._samples_generator import make_blobs

X,y=make_blobs(n_samples=50,centers=2,random_state=0,cluster_std=0.6)

import matplotlib.pyplot as plt


plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="autumn")
plt.show()

from sklearn.svm import SVC 

prediction=SVC(kernel="linear",C=1E10)
prediction.fit(X,y)

from sklearn.datasets._samples_generator import make_circles

X,y=make_circles(100,factor=.1,noise=.1)

clf=SVC(kernel="linear").fit(X,y)
clf=SVC(kernel="rbf",C=1E6,gamma="auto").fit(X,y)

#C ve gamma arttırarak model kompleksleşir ve daha doğru sonuç verebilir.
