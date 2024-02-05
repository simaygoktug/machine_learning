#Çok karmaşık bir soru çok fazla sıradan insana sorulduğunda, bir uzmandan daha doğru bir cevap elde edilebilir.
#Buna kalabalığın zekası denir.

#Farklı algoritmalar kullanıp en çok çıkan sonuca göre tahmine karar verilir.

from sklearn.datasets import make_moons

X,y=make_moons(n_samples=100,noise=0.25,random_state=3)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,stratify=y)

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 

log=LogisticRegression(solver="lbfgs").fit(X_train,y_train)
rnd=RandomForestClassifier(n_estimators=10).fit(X_train,y_train)
svm=SVC(gamma="auto").fit(X_train,y_train)
voting=VotingClassifier(estimators=[("lr",log),("rf",rnd),("svc",svm)],voting="soft").fit(X_train,y_train)

print(log.score(X_test,y_test))
print(rnd.score(X_test,y_test))
print(svm.score(X_test,y_test))
print(voting.score(X_test,y_test))
