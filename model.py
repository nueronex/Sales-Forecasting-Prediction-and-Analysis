import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# === Load your dataset ===
df = pd.read_csv("/content/features.csv")

# === Features & Target ===
print(df.columns)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print(df.columns.tolist())

# Corrected features and target based on available columns
X = df[['temperature', 'fuel_price', 'cpi']]
y = df['unemployment']

# === Impute missing values in the target variable y ===
y_imputer = SimpleImputer(strategy='mean')
y = y_imputer.fit_transform(y.values.reshape(-1, 1)).ravel() # Reshape for imputer and flatten back

# === Preprocessing for Categorical Features ===
categorical_features = []
numeric_features = ['temperature', 'fuel_price', 'cpi']

# Create a preprocessor with an imputer for numeric features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ],
    remainder='passthrough'
)

# === Build Pipeline with Linear Regression ===
pipeline = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('regressor', LinearRegression())
])

# === Split Data ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=52)

# === Train Model ===
pipeline.fit(X_train, y_train)

# === Evaluate ===
score = pipeline.score(X_test, y_test)
print(f"Model R^2 Score: {score:.2f}")
print(f"model rmse score:{score : .3f}")
print(f"moel mae score:{score :.3f}")
# === Save the trained model ===
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/model.pkl")
print("Model saved to models/model.pkl")
