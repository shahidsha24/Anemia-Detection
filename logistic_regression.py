# -*- coding: utf-8 -*-
"""Logistic Regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A5iOWh3_Ustxu95IP6Idg3pJA2nlz0Tl
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt



df=pd.read_csv(r"/content/sample_data/anemia.csv")

from google.colab import drive
drive.mount('/content/drive')

df.head()

df.tail(10)



df

df.drop_duplicates()

df=df.dropna() #balaji

df['MCH'].value_counts()

df['Gender'].value_counts()

df['Hemoglobin'].mean()

df['Hemoglobin'].std()

df['Gender'].std()

df['Gender'].mode()

df['Hemoglobin'].min()

df.isnull().sum()

plt.figure(figsize=(20,15), facecolor='white')
plotnumber = 1

for column in df:
    if plotnumber<=8 :
        ax = plt.subplot(3,3,plotnumber)
        sns.histplot(df[column])
        plt.xlabel(column,fontsize=20)
    plotnumber+=1
plt.tight_layout()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Hemoglobin',y='MCV',hue='MCHC', data=df, s=150)
plt.title("MCHC", y=1.015, fontsize=20)
plt.xlabel("Hemoglobin", labelpad=13) #the spacing in points from the axes bounding box including ticks and tick labels
plt.ylabel("MCV", labelpad=13)
ax = plt.gca()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='MCH',y='MCV',hue='MCHC', data=df, s=150)
plt.title("MCHC", y=1.015, fontsize=20)
plt.xlabel("MCHC", labelpad=13) #the spacing in points from the axes bounding box including ticks and tick labels
plt.ylabel("MCV", labelpad=13)
ax = plt.gca()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='MCH',y='MCV',hue='Gender', data=df, s=150)
plt.title("Gender", y=1.015, fontsize=20)
plt.xlabel("MCH", labelpad=13) #the spacing in points from the axes bounding box including ticks and tick labels
plt.ylabel("MCV", labelpad=13)
ax = plt.gca()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Result',y='MCH',hue='Gender', data=df, s=150)
plt.title("Anemia", y=1.015, fontsize=20)
plt.xlabel("Result", labelpad=13) #the spacing in points from the axes bounding box including ticks and tick labels
plt.ylabel("MCH", labelpad=13)
ax = plt.gca()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')   #Subplot-Add an Axes to the current figure or retrieve an existing Axes.

for s in df.Result.unique():
    ax.scatter(df.Gender[df.Result==s],df.MCH[df.Result==s],df['Hemoglobin'][df.Result==s],label=s)

ax.legend()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')   #Subplot-Add an Axes to the current figure or retrieve an existing Axes.

for s in df.Result.unique():
    ax.scatter(df.Gender[df.Result==s],df.MCH[df.Result==s],df['MCV'][df.Result==s],label=s)

ax.legend()

sns.violinplot(data=df,x='Gender',y='Result')

sns.scatterplot(data=df,x='Gender',y='MCH')

ax= plt.subplots(figsize=(15,10))
sns.boxplot(data=df, width= 0.5,  fliersize=3)

x = df.drop('Result', axis=1)
y = df['Result']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

anemia=LogisticRegression(random_state= 0)
anemia.fit(x_train,y_train)

y_pred = anemia.predict(x_test)

y_pred

x_test

y_test

cm=confusion_matrix(y_test,y_pred)

def sigmoid(x):
  return(1/(1 + np.exp(-x)))

x_values_for_sigmoid=np.linspace(-10,10)
plt.figure(figsize=(8,7))
plt.plot(x_values_for_sigmoid, sigmoid(x_values_for_sigmoid), c='teal')
plt.title('Sigmoid Function')
plt.grid(True)
plt.text(2,8.3,r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=26)
plt.show()

cm

true_positive = cm[0][0]
false_positive = cm[0][1]
false_negative = cm[1][0]
true_negative = cm[1][1]

Accuracy = (true_positive + true_negative) / (true_positive +false_positive + false_negative + true_negative)
Accuracy

Precision = true_positive/(true_positive+false_positive)
Precision

Recall = true_positive/(true_positive+false_negative)
Recall

F1_Score = 2*(Recall * Precision) / (Recall + Precision)
F1_Score

bal=anemia.predict([[1,14.7,22,28.2,99.5]])
bal

IKII=anemia.predict([[1,16,21,40,91.5]])
IKII

Shau=anemia.predict([[1,1,1,1.2,1]])
Shau

anemia.predict(x_test)

x_test_data = x_test
print("x_test data:")
print(x_test_data)

accuracy=accuracy_score(y_test,y_pred)
accuracy

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

plt.plot(fpr, tpr, color='orange', label='ROC')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--',label='ROC curve (area = %0.2f)' % auc)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show()

auc=roc_auc_score(y_test,y_pred)
auc

sns.heatmap(df.corr(),cbar=True)

sns.distplot(df.Hemoglobin)

sns.countplot(data=df,x="Gender",hue="Result")