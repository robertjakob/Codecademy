import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean',]
outcome_var='diagnosis'

x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3)
print('Train positivity rate: ')
print(sum(y_train)/y_train.shape[0])
print('Test positivity rate: ')
print(sum(y_test)/y_test.shape[0])

## 1. Stratified Sampling
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3, stratify=df[outcome_var])
print('Train positivity rate: ')
print(sum(y_train)/y_train.shape[0])
print('Test positivity rate: ')
print(sum(y_test)/y_test.shape[0])

log_reg = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001)
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
print(f'Recall Score: {recall_score( y_test, y_pred)}')
print(f'Accuracy Score: {accuracy_score( y_test, y_pred)}')


#2. Balanced Class weights
log_reg = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001, class_weight='balanced')
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
print(f'Recall Score: {recall_score( y_test, y_pred)}')
print(f'Accuracy Score: {accuracy_score( y_test, y_pred)}')

#3. Over/under-sampling
df_oversample = df[df[outcome_var]==1].sample(df[df[outcome_var]==0].shape[0], replace=True)
new_os_df = pd.concat([df[df[outcome_var]==0], df_oversample])
print('Oversampled class counts:')
print(new_os_df[outcome_var].value_counts())
