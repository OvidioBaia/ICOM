import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

data = pd.read_csv("spotify.csv")
caracteristicas = data[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'classes']]
classes = caracteristicas[['classes']]

unique, counts = np.unique(classes, return_counts=True)
print(unique)
print(counts)

min_max_scaler = preprocessing.MinMaxScaler()
caracteristicas = min_max_scaler.fit_transform(caracteristicas)
caracteristicas


total_acc = 0.0
total_prec = 0.0
total_f1 = 0.0
total_recall = 0.0

for i in range(10):
    
    X_train, X_test, y_train, y_test = train_test_split(caracteristicas, classes, test_size=0.2)
    knn = KNeighborsClassifier(n_neighbors=7, metric="euclidean")
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")
    recall = recall_score(y_test, y_pred, average="macro")
    total_acc += acc
    total_prec += prec
    total_f1 += f1
    total_recall += recall
    
    print("%d° - %0.3f %0.3f %0.3f %0.3f " % (i+1,acc, prec, f1, recall))
    
print("\nResultado\n%0.3f %0.3f %0.3f %0.3f" % (total_acc/10,total_prec/10,total_f1/10,total_recall/10) )