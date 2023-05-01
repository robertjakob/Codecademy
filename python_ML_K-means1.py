#BUILD A MACHINE LEARNING MODEL WITH PYTHON
#Handwriting Recognition using K-Means

import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

 
digits = datasets.load_digits()
#print(digits)
#print(digits.DESCR)
#print(digits.data)
#print(digits.target)

# Figure size (width, height)
 
fig = plt.figure(figsize=(6, 6))
 
# Adjust the subplots 
 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
 
# For each of the 64 images
 
for i in range(64):
 
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
 
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
 
    # Display an image at the i-th position
 
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
 
    # Label the image with the target value
 
    ax.text(0, 7, str(digits.target[i]))
 
plt.show()

model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

fig = plt.figure(figsize=(8, 3))
 
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')


for i in range(10):
 
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
 
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
[0.00,0.00,0.00,0.15,1.83,4.50,3.66,0.08,0.00,0.00,1.07,6.56,7.62,7.17,7.63,3.36,0.00,0.00,3.21,7.09,2.44,0.31,5.95,5.87,0.00,0.00,0.08,0.46,0.00,0.08,6.71,4.96,0.00,0.00,0.00,0.00,0.00,2.90,7.62,2.21,0.00,0.00,0.00,0.00,0.61,6.71,7.24,1.83,0.00,0.00,0.00,0.31,6.79,7.62,7.63,4.43,0.00,0.00,0.00,0.00,3.36,2.60,0.69,0.00],
[0.00,0.00,0.00,0.00,0.84,0.99,0.00,0.00,0.00,0.00,0.00,2.14,7.40,7.63,5.72,1.22,0.00,0.00,1.60,7.40,5.95,3.36,7.09,5.80,0.00,0.00,3.59,7.63,0.54,2.06,7.47,4.12,0.00,0.00,2.29,7.62,5.95,7.62,6.41,0.53,0.00,0.00,0.15,5.72,7.40,3.59,0.23,0.00,0.00,0.00,0.00,0.08,0.53,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.38,7.17,2.90,0.00,0.00,0.00,0.00,2.06,7.17,7.62,4.42,0.00,0.00,0.00,2.98,7.55,6.18,6.64,5.34,0.00,0.00,0.00,7.10,5.49,0.23,6.71,5.04,0.00,0.00,0.00,0.99,0.23,0.00,7.48,3.97,0.00,0.00,0.00,0.00,0.00,0.00,2.29,0.76,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.76,6.79,7.62,7.55,2.75,0.00,0.00,0.00,3.97,7.55,1.98,5.57,7.17,0.00,0.00,0.00,5.87,7.02,2.06,0.23,0.99,0.00,0.00,0.00,5.27,7.55,7.62,3.89,0.00,0.00,0.00,0.00,0.00,0.92,7.47,4.73,0.00,0.00,0.00,0.46,2.75,6.03,7.32,0.92,0.00,0.00,0.00,3.05,7.62,6.64,1.98,0.00,0.00,0.00,0.00,0.08,0.76,0.08,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)
 
print(new_labels)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')


