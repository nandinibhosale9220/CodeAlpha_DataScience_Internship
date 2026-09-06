# CodeAlpha Data Science Internship
# Task 2: Unemployment Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Unemployment in India.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Sort data by date
df = df.sort_values("Date")

print("\nDate Column Data Type:")
print(df["Date"].dtype)

print("\nDate Range:")
print(df["Date"].min(), "to", df["Date"].max())

# Plot overall unemployment rate trend

monthly_unemployment = df.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean()

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker="o"
)

plt.title("Unemployment Rate Trend in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save the graph
plt.savefig("unemployment_rate_trend.png", dpi=300)

plt.show()

# COVID-19 Impact Analysis

# Define COVID-19 period
covid_period = df[
    (df["Date"] >= "2020-03-01") &
    (df["Date"] <= "2020-06-30")
]

# Calculate average unemployment rate
covid_avg = covid_period["Estimated Unemployment Rate (%)"].mean()

pre_covid = df[df["Date"] < "2020-03-01"]
pre_covid_avg = pre_covid["Estimated Unemployment Rate (%)"].mean()

print("\nCOVID-19 Impact Analysis:")
print(f"Average unemployment rate before COVID-19: {pre_covid_avg:.2f}%")
print(f"Average unemployment rate during COVID-19: {covid_avg:.2f}%")
print(f"Increase in unemployment rate: {covid_avg - pre_covid_avg:.2f}%")

# COVID-19 Impact Visualization

plt.figure(figsize=(10, 6))

plt.plot(
    covid_period["Date"],
    covid_period["Estimated Unemployment Rate (%)"],
    marker="o"
)

plt.title("COVID-19 Impact on Unemployment Rate in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save the graph
plt.savefig("covid19_unemployment_impact.png", dpi=300)

plt.show()

# Region-wise Unemployment Rate

region_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 7))

plt.barh(
    region_unemployment.index,
    region_unemployment.values
)

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("Region")

plt.tight_layout()
plt.savefig("region_wise_unemployment.png", dpi=300)
plt.show()