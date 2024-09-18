import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Find the maximum length of the sequences
max_length = max(len(np.ravel(d)) for d in data_dict['data'])

# Pad the sequences to the maximum length
data = np.array([np.pad(np.ravel(d), (0, max_length - len(np.ravel(d))), mode='constant') for d in data_dict['data']])

# Labels
labels = np.asarray(data_dict['labels'])

# Split the data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train the RandomForest model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict and evaluate
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
