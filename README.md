# Machine Learning

Study scripts and notes covering classical machine learning, data preparation, pandas exercises and MLOps basics, organised by topic.

## Overview

Each folder holds a short, self-contained script (usually `ml_1.py`) on one topic, mostly built with scikit-learn on standard datasets such as Iris, Breast Cancer and synthetic moons or blobs. Code comments are written in Turkish. Some folders contain screenshots of notes instead of code, and the `mlops/` files are annotated notes that mix code with install instructions, so they are meant to be read rather than run directly.

## Contents

| Folder | Description |
| --- | --- |
| `data_preprocessing/` | Cleaning the Google Play Store dataset with pandas and seaborn (`googleplaystore.csv` included) |
| `data_visualizing/` | Exploratory plots of a Forbes 2022 billionaires dataset |
| `data_scaling/` | `MinMaxScaler` on the Breast Cancer dataset |
| `linear_r/` | Linear regression on student performance data (`student-mat.csv` included) |
| `logistic_r/` | Logistic regression on Breast Cancer |
| `ridge_lasso/` | Ridge regression on extended Boston housing (mglearn) |
| `k_nn/` | k-nearest neighbours with mglearn forge data, plus note screenshots |
| `decision_trees/` | Decision trees on Iris and Breast Cancer with Graphviz export, plus note screenshots |
| `random_forests/` | Random forest and voting classifier on moons data |
| `support_vector_machines/` | SVC on blobs and circles |
| `naive_bayes/` | Gaussian Naive Bayes on blobs |
| `mlp_classifier/` | scikit-learn `MLPClassifier` on moons data |
| `gaussian_mixture_models/` | Photographed notebook notes on clustering and GMMs |
| `cross_validation/` | K-fold cross-validation and train/test evaluation on Iris |
| `pipelines/` | scikit-learn pipelines with scaling, feature selection and SVMs |
| `text_mining/` | Bag-of-words and TF-IDF with Multinomial Naive Bayes on a local text dataset folder (path set in the script) |
| `pycaret/` | PyCaret classification on a heart disease dataset with random oversampling |
| `bigquery/` | Notes on training and evaluating a BigQuery ML linear regression on the public penguins dataset |
| `gnu_octave/` | Linear regression cost function in Octave with sample feature and price data |
| `pytorch/` | Screenshots of PyTorch linear regression and binary classifier examples |
| `pandas/` | 42 function-style pandas exercises: filtering, groupby, merging, melting, pivoting, ranking and string validation |
| `mlops/` | Notes and examples on Flask model APIs, Prometheus monitoring, Kubeflow pipelines, hyperparameter search, ARIMA forecasting, BERT sentiment analysis and OOP |

## Tech stack

- Python, scikit-learn, pandas, NumPy, Matplotlib, seaborn, mglearn
- PyCaret, imbalanced-learn, statsmodels
- TensorFlow, PyTorch, Hugging Face Transformers
- Flask, Prometheus client, Kubeflow Pipelines
- Google BigQuery ML, GNU Octave

## How to run

Most scripts run on their own from inside their folder, for example:

```bash
cd logistic_r
python ml_1.py
```

Scripts that read a CSV expect the file in the same folder. Only `googleplaystore.csv` and `student-mat.csv` are included; the Forbes, heart disease and text datasets must be supplied separately. Some examples use `load_boston`, which was removed in scikit-learn 1.2, so they need an older scikit-learn.

## Author

Goktug Can Simay: [GitHub](https://github.com/simaygoktug) | [Website](https://goktugcansimay.com)
