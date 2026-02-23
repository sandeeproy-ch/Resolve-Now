# 🛡️ Online Fraud Detection System

A Machine Learning based web application that detects fraudulent financial transactions using classification algorithms.  
The system predicts whether a transaction is Fraudulent or Legitimate based on transaction details.

---

## 📌 Project Description

Online financial fraud has increased significantly with digital transactions.  
This project aims to detect fraudulent transactions using supervised machine learning algorithms.

The model is trained on transaction data and deployed using Flask to provide real-time fraud prediction via a web interface.

---

## 🎯 Project Objectives

- Understand fraud detection using Machine Learning
- Perform data preprocessing and feature engineering
- Train multiple classification models
- Compare model performance
- Deploy the best model using Flask
- Provide real-time prediction through web UI

---

## 🧠 Machine Learning Models Used

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Each model was evaluated using:

- Accuracy
- Confusion Matrix
- Classification Report

The best performing model was selected and saved using pickle.

---

## 📊 Dataset

Dataset used: Financial Fraud Transaction Dataset  
Target column: `isFraud`

Main features include:

- step
- type
- amount
- oldbalanceOrg
- newbalanceOrig
- oldbalanceDest
- newbalanceDest

---

## ⚙️ Technologies Used

### Programming Language
- Python 3.x

### Libraries
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn
- pickle
- Flask

### Tools
- Anaconda
- VS Code / PyCharm
- Git & GitHub
- Render (for deployment)

---

## 🏗️ Project Structure
online_fraud/
│

├── fraud.csv

├── train_model.py

├── app.py

├── model.pkl

├── encoder.pkl

├── scaler.pkl

├── requirements.txt
│

├── templates/

│ ├── home.html

│ ├── predict.html

│ └── submit.html

│

└── static/


---

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Handling Missing Values
4. Encoding Categorical Variables
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Save Model (model.pkl)
10. Flask Integration
11. Deployment

---

## 🖥️ Installation & Setup

### Step 1: Clone Repository



[git clone https://github.com/Prem-0427/online_fraud_payment]

cd online-fraud-detection


### Step 2: Create Virtual Environment



conda create -n fraud_env python=3.10
conda activate fraud_env


### Step 3: Install Requirements

pip install -r requirements.txt


---

## ▶️ Running the Application

### Step 1: Train Model



python train_model.py


This will generate:
- model.pkl
- encoder.pkl
- scaler.pkl

### Step 2: Run Flask App
python app.py
Open browser:

http://127.0.0.1:5000/


---

## 🌐 Deployment

The application can be deployed on:

- Render
- IBM Cloud
- Heroku
- AWS EC2

Deployment Steps (Render):

1. Push code to GitHub
2. Connect GitHub to Render
3. Add Build Command:


pip install -r requirements.txt

4. Add Start Command:


python app.py


---

## 🔐 Features

- Real-time fraud prediction
- Multiple ML model comparison
- Clean user interface
- Scalable deployment
- High accuracy prediction

---

## 📈 Model Performance

Example (Random Forest):

- Accuracy: ~95%
- Precision: High
- Recall: High
- F1 Score: Balanced

---

## 🧪 Testing

- Manual Testing
- Model Evaluation Metrics
- Confusion Matrix Analysis
- Cross Validation

---

## ⚠️ Known Issues

- Large dataset increases training time
- Requires significant memory for full dataset
- Model accuracy depends on data quality

---

## 🚀 Future Enhancements

- Real-time transaction API integration
- Deep Learning model implementation
- Fraud pattern visualization dashboard
- Role-based authentication
- Cloud auto-scaling deployment

---

## 👨‍💻 Team Details

- Team ID: LTVIP2026TMIDS63406  
- Team Leader: Anda Tharun  
- Team Member: Mannaru Prem Kumar  
- Team Member: Chavva Tarun  
- Team Member: Gaduputi Hima Varshini  

---

## 📌 Conclusion

This project demonstrates how Machine Learning can effectively detect fraudulent transactions and reduce financial risk.  
The system is scalable, efficient, and ready for real-world deployment.

---

## 📎 License

This project is for educational purposes.
