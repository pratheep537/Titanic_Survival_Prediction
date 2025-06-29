# 🚢 Titanic Survival Prediction Web App

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Internship](https://img.shields.io/badge/Internship-Afido%20Tech-red)

## 📌 Project Overview

This project is a responsive web-based **Titanic Survival Predictor**, built using **Machine Learning** and **Flask**.

It was developed as **Task 3 of my internship at Afido Tech**, with the goal of learning how to preprocess real-world data, build an end-to-end ML model, and deploy it through a user-friendly web interface.

The app predicts whether a passenger would have **survived the Titanic disaster** based on the following inputs:
- Passenger Class (Pclass)
- Gender
- Age
- Fare
- Port of Embarkation
- Number of Siblings/Spouses Aboard
- Number of Parents/Children Aboard

---

## 🎯 Key Highlights

- ✅ Model: `LogisticRegression` from `scikit-learn`
- ✅ Dataset: Titanic dataset from [Kaggle](https://www.kaggle.com/c/titanic/data)
- ✅ Accuracy: Achieved ~80% on test set using feature engineering
- ✅ Feature Engineering: Title extraction, family size, isolation flag
- ✅ Tech Stack: Python, Flask, HTML/CSS, Bootstrap
- ✅ UI/UX: Custom Titanic-themed background, styled form

---

## 🔍 Learning Outcomes

During this project, I explored:
- Data cleaning, imputation, and transformation
- Categorical encoding and numeric scaling via pipelines
- Building robust ML pipelines using `ColumnTransformer`
- Flask integration with ML predictions
- Styling using Bootstrap and fixed backgrounds
- Git & GitHub version control

---

## 🖼 Screenshots

![Prediction Screenshot](./static/prediction_demo.png)  
![Web App UI](./static/website_preview.png)

---

## 🛠 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/titanic-prediction.git
cd titanic-prediction
