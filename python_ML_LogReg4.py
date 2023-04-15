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
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)


log_reg = LogisticRegression(penalty='none', fit_intercept=True,tol=0.0000001,solver='newton-cg')

log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
y_pred_prob = log_reg.predict_proba(x_test)


plt.figure(figsize=(8,6))
plt.hist(y_pred_prob[y_test==0,1], alpha=.5, label='Benign',)
plt.hist(y_pred_prob[y_test==1,1], alpha=.5 , label='Malignant')
plt.xlabel('Predicted Probability', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.plot([.25, .25],[0,50],color='grey', linestyle=':')
plt.plot([.5, .5],[0,50],color='grey', linestyle=':')
plt.plot([.75, .75],[0,50],color='grey', linestyle=':')
plt.ylim([0,50])
plt.legend()
plt.title('Histogram of Malignant and Benign \nPredicted Probabilities from LR Model', fontsize=14)
plt.show()

## Using the predicted probabilities to get the predicted class
y_pred_class = (y_pred_prob[:,1]>0.5)*1.0

##1. Check if it's the same as the predicted class obtained using .predict()
print(abs(y_pred_class-y_pred).sum())

##2a.Changing the threshold now to be 0.25
print("Confusion Matrix: Threshold 0.25")
y_pred_class = (y_pred_prob[:,1]>0.25)*1.0
print(confusion_matrix( y_test, y_pred_class))

print("Confusion Matrix: Threshold 0.5")
y_pred_class = (y_pred_prob[:,1]>0.5)*1.0
print(confusion_matrix( y_test, y_pred_class,))

## 2b. Change the threshold to be 0.75 and compare it to the above
print("Confusion Matrix: Threshold 0.75")
y_pred_class = (y_pred_prob[:,1]>0.75)*1.0
print(confusion_matrix( y_test, y_pred_class))

#create an array of threshold values between 0 and 1
thresh = np.linspace(0,1, 100)
#number of positive test cases
pos_cases = y_test.sum()

#3. Calculate the false negative rate for each threshold
fn_rate = [1 - sum(y_pred_prob[y_test==1][:,1]>t)/pos_cases for t in thresh]
#Find the first threshold value where the is greater than 2 per 100
max_thresh = thresh[np.argmax(np.array(fn_rate)>0.02)]
print(f'Max Threshold for less than 2 per 100 FNs:{max_thresh}')
