import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from joblib import dump, load

FILE_NAME = '15_minutes.csv'
TRAIN_LABELS = ['time', 'open', 'close', 'low', 'high', 'MovingAverage20', 'MovingAverage50', 'MovingAverage100']
TEST_LABEL = 'ShouldBuy'
CSV_PATH = 'data_to_train/'+FILE_NAME
MODEL_PATH = 'models/'+FILE_NAME.replace('.csv', '.joblib')

# Load the dataset
def load_data(csv_path):
    data = pd.read_csv(csv_path)
    X = data[TRAIN_LABELS]
    y = data[TEST_LABEL]
    return X, y

# Train the model
def train_model(X, y, n_estimators=100, random_state=42):
    print("Training Model")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    clf = RandomForestClassifier(
        n_estimators=n_estimators, 
        random_state=random_state, 
        verbose=2, 
        n_jobs=5
        )
    clf.fit(X_train, y_train)
    return clf

# Predict data from a CSV file
def predict_from_csv(csv_path, model_path):
    X, _ = load_data(csv_path)
    clf = load(model_path)
    y_pred = clf.predict(X)
    
    return y_pred

# Predict data from literals
def predict_from_literals(time, open_price, close_price, low_price, high_price, volume, moving_average_20, moving_average_50, moving_average_100, model_path):
    clf = load(model_path)
    X = pd.DataFrame([[time, open_price, close_price, low_price, high_price, volume, moving_average_20, moving_average_50, moving_average_100]], columns=TRAIN_LABELS)
    y_pred = clf.predict(X)
    return y_pred

# Example usage
# Load the dataset
X, y = load_data(CSV_PATH)

# Train the model
clf = train_model(X, y)

# Save the model
dump(clf, MODEL_PATH)

# Predict from a CSV file
y_pred_csv = predict_from_csv(CSV_PATH, MODEL_PATH)
print("Predictions from CSV:", y_pred_csv)
print("Accuracy", accuracy_score(y, y_pred_csv))
# Predict from literals
# y_pred_literals = predict_from_literals(1633062400000, 8285.45, 8292.1, 8285.45, 8295.9, 0, 8285.45, 8292.1, 8295.9, MODEL_PATH)
# print("Predictions from literals:", y_pred_literals)
