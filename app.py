
from flask import Flask, render_template, request
import pickle
import numpy as np
from utils.feature_extraction import extract_features_from_url

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model_data = pickle.load(file)

feature_names = None  # Not available

model = model_data["model"]
feature_names = model_data["features"]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    url = ''
    error_message = None
    feature_analysis = None

    if request.method == 'POST':
        url = request.form['url']
        try:
            features_data = extract_features_from_url(url, return_details=True)
            features = features_data["values"]
            feature_analysis = features_data["analysis"]

            features = np.array(features).reshape(1, -1)
            pred = model.predict(features)[0]
            prediction = 'Legitimate Website 🟢' if pred == 1 else 'Phishing Website ⚠️'
        except Exception as e:
            error_message = f"Error: Unable to process the URL. ({str(e)})"

    return render_template('index.html', prediction=prediction, url=url, error_message=error_message, feature_analysis=feature_analysis)


if __name__ == '__main__':
    app.run(debug=True)
