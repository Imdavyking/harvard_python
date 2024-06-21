import csv
import random
import tensorflow as tf
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

model = Perceptron()

with open('banknotes.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    data = []

    for row in reader:
        data.append({
            'evidence': [float(cell) for cell in row[:4]],
            'label': 1 if row[4] == '0' else 0
        })

evidence = [row['evidence'] for row in data]
labels = [row['label'] for row in data]

X_training,X_testing,y_training,y_testing = train_test_split(evidence,labels,test_size=0.4)
X_training = np.array(X_training)
X_testing = np.array(X_testing)
y_training = np.array(y_training)
y_testing = np.array(y_testing)
model = tf.keras.models.Sequential()
# Add a hidden layer with 8 units with ReLU activation
model.add(tf.keras.layers.Dense(8, input_shape=(4,),activation='relu'))

# Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(1,activation='sigmoid'))

# Train neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


model.fit(X_training,y_training,epochs=20)

# # # Evaluate how well model performs
model.evaluate(X_testing,y_testing,verbose=2)



