import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
df = pd.read_csv("Advertising.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# 2. Remove unnecessary column
df = df.drop("Unnamed: 0", axis=1)


# 3. Display statistical summary
print("\nStatistical Summary:")
print(df.describe())


# 4. Define features and target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]


# 5. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 6. Create Linear Regression model
model = LinearRegression()


# 7. Train model
model.fit(X_train, y_train)


# 8. Make predictions
y_pred = model.predict(X_test)


# 9. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))
print("R² Score:", round(r2, 2))


# 10. Display model coefficients
print("\nAdvertising Impact:")
print("TV coefficient:", round(model.coef_[0], 3))
print("Radio coefficient:", round(model.coef_[1], 3))
print("Newspaper coefficient:", round(model.coef_[2], 3))


# 11. Actual vs Predicted Sales
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.grid(True)

plt.savefig("actual_vs_predicted_sales.png")
plt.show()


# 12. Advertising impact visualization
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Advertising and Sales")

plt.savefig("advertising_correlation.png")
plt.show()