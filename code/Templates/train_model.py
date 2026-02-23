import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("fraud.csv")

# Use only important fraud features
df = df[["step","type","amount","oldbalanceOrg","newbalanceOrig",
         "oldbalanceDest","newbalanceDest","isFraud"]]

# Encode type
le = LabelEncoder()
df["type"] = le.fit_transform(df["type"])

# Features & target
X = df.drop("isFraud", axis=1)
y = df["isFraud"]

# Balance the dataset (fraud is rare!)
fraud = df[df.isFraud == 1]
safe = df[df.isFraud == 0].sample(len(fraud)*3)

df_balanced = pd.concat([fraud, safe])

X = df_balanced.drop("isFraud", axis=1)
y = df_balanced["isFraud"]

# Train
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)

# Save
pickle.dump(model, open("model.pkl","wb"))
pickle.dump(le, open("encoder.pkl","wb"))

print("Model trained successfully")
