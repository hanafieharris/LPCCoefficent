import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
#matplotlib inline 
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.utils import shuffle
import warnings

warnings.filterwarnings('ignore')
#df = pd.read_csv('Data Training.csv')

train = pd.read_csv("Data Training.csv")
test  = pd.read_csv("Test_data4F.csv")

#df = df.drop(['Coef1','Coef2','Coef3','coef4','coef5','coef6', 'coef7', 'coef8','coef9','coef10','coef11','coef12','coef13'], axis=1)
#df.head()
                      
#y = df['classs']
#x = df.drop(['classs'], axis=1)
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.4, random_state=30)

X_train = pd.DataFrame(train.drop(['classs'],axis=1))
Y_train = train.classs.values.astype(object)
X_test = pd.DataFrame(test.drop(['classs'],axis=1))
Y_test = test.classs.values.astype(object)

clf = MLPClassifier(
                    solver='lbfgs',
                    activation='relu',
                    alpha=1e-4,
                    hidden_layer_sizes=(13),
                    random_state=2,
                    max_iter=1000,
                    learning_rate_init = 0.01,
                    tol=1e-4,
                    )

clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
accuracy_score(Y_test, y_pred)
cm = confusion_matrix(Y_test, y_pred)
print("Data Training : ")
print(train)
print("Data Testing : ")
print(test)
print("Result...")
print("---------------------------")
print("")
print("Confusion Matrix")
print(cm)
print("")
print("---------------------------")
print("")
print("SCORE : " + str(accuracy_score(Y_test, y_pred)))
print("")
print("---------------------------")
#print(clf.fit)