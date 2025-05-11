import pandas as pd
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load your dataset
df = pd.read_csv('phising_08012020_120000.csv')

# ✅ Convert -1 to 0
df['Result'] = df['Result'].replace(-1, 0)

# Split into Features and Labels
X = df.drop('Result', axis=1)
y = df['Result']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Model trained! Test Accuracy: {accuracy * 100:.2f}%")

# Save the model
# Save model + features
model_data = {
    "model": model,
    "features": X.columns.tolist()
}

with open('model.pkl', 'wb') as file:
    pickle.dump(model_data, file)

print("✅ Model and features saved as model.pkl")

