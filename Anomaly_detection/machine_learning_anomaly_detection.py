import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the CSV data
data = pd.read_csv('serial_data.csv')

# Define threshold values for anomaly detection
anomaly_threshold_high = 1000
anomaly_threshold_low = 10

# Label data based on anomaly thresholds
data['status'] = 'normal'
data.loc[(data['value'] >= anomaly_threshold_high) | (data['value'] <= anomaly_threshold_low), 'status'] = 'anomaly'
data.loc[(data['value'] < anomaly_threshold_high) | (data['value'] > anomaly_threshold_low), 'status'] = 'normal'

# Prepare feature matrix X and target vector y
X = data[['value']]
y = data['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model (Random Forest classifier)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'anomaly_detection_model.pkl')

print(data.to_string())