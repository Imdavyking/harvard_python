import csv
import random

from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = Perceptron()

with open('banknotes.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    data = []

    for row in reader:
        data.append({
            'evidence': [float(cell) for cell in row[:4]],
            'label': 'Authentic' if row[4] == '0' else 'Counterfeit'
        })

holdout = int(0.5 * len(data))
random.shuffle(data)
testing = data[holdout:]
training = data[:holdout]

X_training = [row['evidence'] for row in training]
y_training = [row['label'] for row in training]
model.fit(X_training, y_training)

X_testing = [row['evidence'] for row in testing]
y_testing = [row['label'] for row in testing]
predictions = model.predict(X_testing)

correct = 0
incorrect = 0

total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"InCorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")



