#BUILD DEEP LEARNING MODELS WITH TENSORFLOW
#Implementing Neural Networks

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


dataset  = pd.read_csv('life_expectancy.csv')

print(dataset.head())
print(dataset.describe())

dataset = dataset.drop(["Country"], axis = 1)

labels = dataset.iloc[:, -1] #select all the rows (:), and access the last column (-1)

features = dataset.iloc[:, 0:-1] #select all the rows (:), and access columns from 0 to the last column

features = pd.get_dummies(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state=23)

numerical_features = features.select_dtypes(include=['float64', 'int64'])
numerical_columns = numerical_features.columns
 
ct = ColumnTransformer([("only numeric", StandardScaler(), numerical_columns)], remainder='passthrough')

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

my_model = Sequential()
input = InputLayer(input_shape = (features.shape[1], ))

my_model.add(input)
my_model.add(Dense(64, activation = "relu"))
my_model.add(Dense(1))

print(my_model.summary())
opt = Adam(learning_rate = 0.01)
my_model.compile(loss = 'mse', metrics = ['mae'], optimizer = opt)

my_model.fit(features_train_scaled, labels_train, epochs = 50, batch_size = 1, verbose = 1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose = 0)

print(res_mse, res_mae)
