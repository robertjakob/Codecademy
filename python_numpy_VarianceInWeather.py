#ANALYZE DATA WITH PYTHON
#Variance in Weather

import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.head())
print(london_data.tail())
print(len(london_data))

temp = london_data['TemperatureC']

average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

average_temp = np.mean(june)
temperature_var = np.var(june)
temperature_standard_deviation = np.std(june)

average_temp = np.mean(july)
temperature_var = np.var(july)
temperature_standard_deviation = np.std(july)

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

for i in range(0, 24):
  hour = london_data.loc[london_data["hour"] == i]["dailyrainMM"]
  print("The mean rain in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation rain temperature in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")
