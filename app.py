from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('titanic_model.joblib')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    embarked = request.form['embarked']
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])

    # Feature engineering
    family_size = sibsp + parch + 1
    is_alone = 1 if family_size == 1 else 0

    # Create DataFrame for prediction
    data = {
        'Pclass': [pclass],
        'Sex': [sex],
        'Age': [age],
        'Fare': [fare],
        'Embarked': [embarked],
        'Title': ['Mr'],  # Simplified for demo
        'FamilySize': [family_size],
        'IsAlone': [is_alone]
    }

    df = pd.DataFrame(data)

    # Make prediction
    prediction = model.predict(df)
    probability = model.predict_proba(df)[0][1] * 100

    result = {
        'survived': bool(prediction[0]),
        'probability': round(probability, 2),
        'pclass': pclass,
        'sex': sex,
        'age': age,
        'fare': fare,
        'embarked': embarked,
        'sibsp': sibsp,
        'parch': parch
    }

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)