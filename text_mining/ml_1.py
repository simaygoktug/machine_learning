#Bu sefer verimiz metin olacak.

categories=["rec.motorcycles","rec.sport.baseball","comp.graphics","rec.sport.hockey"]

from sklearn.datasets import load_files

twenty_train=load_files("veri_setinin_yolu",categories=categories,shuffle=True,random_state=42,encoding="utf-8",decode_error="ignore")

type(twenty_train)

from sklearn.feature_extraction.text import CountVectorizer

count_vec=CountVectorizer()

X_train_counts=count_vec.fit_transform(twenty_train.data)

###########################################################################

#Şimdi ayrı ayrı dosyalarda en sık geçen kelimeleri tespit eden modeli deneyeceğim.

from sklearn.feature_extraction.text import TfidfTransformer

tf_transformer=TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf=tf_transformer.transform(X_train_counts)

from sklearn.naive_bayes import MultinomialNB

clf=MultinomialNB().fit(X_train_tf,twenty_train.target)

docs_new=["brake-lamp is good","this computer is fast"]

X_new_count=count_vect.transform(docs_new)

X_new_tf=tf_transformer.transform(X_new_count)

predicted=clf.predict(X_new_tf)

for doc,category in zip(docs_new,predicted):
    print("%r=>%s"%(doc,twenty_train.target_names[category]))
