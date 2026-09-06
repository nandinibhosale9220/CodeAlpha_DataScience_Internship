# CodeAlpha Data Science Internship
# Task 3: Car Price Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("car data.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert categorical columns into numerical values

df = pd.get_dummies(
    df,
    columns=["Fuel_Type", "Selling_type", "Transmission"],
    drop_first=True
)

print("\nDataset after encoding:")
print(df.head())

print("\nNew Column Names:")
print(df.columns.tolist())

# Select features and target variable

X = df.drop(["Selling_Price", "Car_Name"], axis=1)
y = df["Selling_Price"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nFeature Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

# Split data into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Shape:")
print(y_train.shape)

print("\nTesting Target Shape:")
print(y_test.shape)


# Train Linear Regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")



# Make predictions
y_pred = model.predict(X_test)

print("\nFirst 10 Actual Prices:")
print(y_test.head(10).values)

print("\nFirst 10 Predicted Prices:")
print(y_pred[:10])

# Model Evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")


# Actual vs Predicted Price Plot
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Prices")

plt.tight_layout()

plt.savefig("actual_vs_predicted.png", dpi=300)

plt.show()