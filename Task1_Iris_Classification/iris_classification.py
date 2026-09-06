# CodeAlpha Data Science Internship
# Task 1: Iris Flower Classification

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# --------------------------------------------------
# 1. Load Iris Dataset
# --------------------------------------------------

iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("First 5 rows of dataset:")
print(X.head())

print("\nDataset shape:")
print(X.shape)

# --------------------------------------------------
# 2. Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# 3. Train Logistic Regression Model
# --------------------------------------------------

model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

# --------------------------------------------------
# 4. Make Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)

# --------------------------------------------------
# 5. Evaluate Model
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# --------------------------------------------------
# 6. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Iris Flower Classification - Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")
plt.tight_layout()

plt.savefig("confusion_matrix.png", dpi=300)
plt.show()

# --------------------------------------------------
# 7. Pair Plot
# --------------------------------------------------

iris_df = X.copy()
iris_df["species"] = [
    iris.target_names[i] for i in y
]

sns.pairplot(
    iris_df,
    hue="species"
)

plt.savefig("iris_pairplot.png", dpi=300)
plt.show()

print("\nTask 1 completed successfully!")