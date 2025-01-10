#Hiperparametre optimizasyonu, makine öğrenmesi modelinizin performansını artırmak için en iyi hiperparametre kombinasyonlarını bulma sürecidir. 
#Bu süreçte en yaygın kullanılan yöntemler:

#Grid Search: Belirli hiperparametre değerlerini sistematik olarak deneyerek en iyi kombinasyonu bulur.
#Random Search: Hiperparametre değerlerini rastgele seçerek daha hızlı bir şekilde sonuç bulmayı hedefler.

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Veri setini yükleme
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hiperparametre aralığını tanımlama
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': [0.1, 1, 10]
}

# Grid Search
grid_search = GridSearchCV(SVC(), param_grid, cv=3)
grid_search.fit(X_train, y_train)

# En iyi parametreler ve doğruluk
print("En iyi parametreler:", grid_search.best_params_)
y_pred = grid_search.predict(X_test)
print("Grid Search ile doğruluk:", accuracy_score(y_test, y_pred))

from sklearn.model_selection import RandomizedSearchCV
import numpy as np

# Hiperparametre aralığını tanımlama
param_dist = {
    'C': np.logspace(-2, 2, 10),
    'kernel': ['linear', 'rbf'],
    'gamma': np.logspace(-2, 2, 10)
}

# Random Search
random_search = RandomizedSearchCV(SVC(), param_distributions=param_dist, n_iter=10, cv=3, random_state=42)
random_search.fit(X_train, y_train)

# En iyi parametreler ve doğruluk
print("En iyi parametreler:", random_search.best_params_)
y_pred = random_search.predict(X_test)
print("Random Search ile doğruluk:", accuracy_score(y_test, y_pred))

#Grid Search Sonuçları:

En iyi parametreler: {'C': 1, 'gamma': 0.1, 'kernel': 'rbf'}
Grid Search ile doğruluk: 0.9666666666666667


#Random Search Sonuçları:

En iyi parametreler: {'C': 10.0, 'gamma': 0.1, 'kernel': 'rbf'}
Random Search ile doğruluk: 0.9666666666666667
