from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))
encoder = pickle.load(open("encoder.pkl","rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict_page')
def predict_page():
    return render_template("predict.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        step = float(request.form['step'])
        type_ = request.form['type']
        amount = float(request.form['amount'])
        oldOrg = float(request.form['oldbalanceOrg'])
        newOrg = float(request.form['newbalanceOrig'])
        oldDest = float(request.form['oldbalanceDest'])
        newDest = float(request.form['newbalanceDest'])
    except:
        return render_template("submit.html", prediction_text="❌ Invalid input")

    # Encode type
    type_encoded = encoder.transform([type_])[0]

    # ML Prediction
    features = np.array([[step, type_encoded, amount, oldOrg, newOrg, oldDest, newDest]])
    ml_prediction = model.predict(features)[0]

    # 🔥 Rule-based fraud detection (bank logic)
    rule_fraud = False

    if (type_ in ["TRANSFER","CASH_OUT"] and 
        oldOrg == amount and newOrg == 0 and
        oldDest == 0 and newDest == 0):
        rule_fraud = True

    # Final decision
    if ml_prediction == 1 or rule_fraud:
        result = "⚠️ Fraudulent Transaction"
    else:
        result = "✅ Safe Transaction"

    return render_template("submit.html", prediction_text=result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
