import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score


data = pd.read_csv("UNR-IDD.csv")
#data.columns
#print(data.shape)
unique, counts = np.unique(data[['Binary Label']], return_counts=True)
print(unique)
print(counts)
data_copia = data
total_acc = 0.0
total_prec = 0.0
total_f1 = 0.0
total_recall = 0.0
normal = data[data['Binary Label'] == "Normal"]
attack = data[data['Binary Label'] == "Attack"]
print(normal.shape)
print(attack.shape)
print("aqui")
new_attack = attack.loc[0:3772]
print(new_attack.shape)
print(new_attack.info())
new_data_frame = pd.concat([normal, new_attack], axis=0)
print(new_data_frame.shape)
def formatData():
    unique_value_port_number = new_data_frame.iloc[:,1].unique()
    dicionario_port_number = dict(zip(unique_value_port_number, range(len(unique_value_port_number))))
    unique_attack = new_data_frame.iloc[:,-1].unique()
    dicionario_attack = dict(zip(unique_attack, range(len(unique_attack))))
    unique_label = new_data_frame.iloc[:,-2].unique()
    dicionario_label = dict(zip(unique_label, range(len(unique_label))))
    new_data = new_data_frame.replace({'Port Number': dicionario_port_number, 'Binary Label': dicionario_attack, 'Label': dicionario_label})
    # print(new_data)
    return new_data

data_normalized = formatData()
classes = data_normalized[['Binary Label']]
#print(data_normalized)
caracteristicas = data_normalized[['Received Packets','Received Bytes','Sent Bytes','Sent Packets','Port alive Duration (S)','Packets Rx Dropped','Packets Tx Dropped','Packets Rx Errors','Packets Tx Errors','Delta Received Packets','Delta Received Bytes','Delta Sent Bytes','Delta Sent Packets','Delta Port alive Duration (S)','Delta Packets Rx Dropped','Delta Packets Rx Errors','Delta Packets Tx Errors','Connection Point','Total Load/Rate','Total Load/Latest','Unknown Load/Rate','Unknown Load/Latest','Latest bytes counter','Table ID','Active Flow Entries','Packets Looked Up','Packets Matched','Max Size']]
def formatData():
    # data_frame_sem_string = data.select_dtypes(exclude=['object'])
    # caracteristicas = data_frame_sem_string.select_dtypes(exclude=['bool'])
    min_max_scaler = preprocessing.MinMaxScaler()
    caracteristicas = min_max_scaler.fit_transform(caracteristicas)


def defineMetodo(metodo):
    if metodo == 'knn':
        return KNeighborsClassifier(n_neighbors=7, metric="euclidean")
    if metodo == 'svm':
       return svm.SVC(kernel='linear')
    if metodo == 'mlp':
        return MLPClassifier(random_state=1,activation='tanh')
    #return metodo_classificacao


def clearMetricas():
    this.total_acc = 0.0
    this.total_prec = 0.0
    this.total_f1 = 0.0
    this.total_recall = 0.0

def processamento(metodo):
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(caracteristicas, classes, test_size=0.2)
        clf = defineMetodo(metodo)
        clf.fit(X_train, y_train.values.ravel())
        y_pred = clf.predict(X_test)  

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="macro")
        f1 = f1_score(y_test, y_pred, average="macro")
        recall = recall_score(y_test, y_pred, average="macro")
        global total_acc
        total_acc += acc
        global total_prec
        total_prec += prec
        global total_f1
        total_f1 += f1
        global total_recall
        total_recall += recall
        
        print("%d° - %0.3f %0.3f %0.3f %0.3f " % (i+1,acc, prec, f1, recall)) 
    print("\nResultado\n%0.3f %0.3f %0.3f %0.3f" % (total_acc/10,total_prec/10,total_f1/10,total_recall/10) )
    #clearMetricas()
    total_acc = 0.0
    total_prec = 0.0
    total_f1 = 0.0
    total_recall = 0.0
def execute(metodo):
    processamento(metodo)


#execute('knn')
execute('svm')
#execute('mlp')