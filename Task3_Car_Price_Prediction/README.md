# Task 3: Car Price Prediction

## Objective

Build a machine learning model to predict the selling price of used cars based on different features such as present price, year, kilometers driven, fuel type, selling type, transmission, and previous owners.

## Dataset

Dataset: Car Data

The dataset contains 301 car records and 9 columns.

### Features

- Car Name
- Year
- Present Price
- Driven Kilometers
- Fuel Type
- Selling Type
- Transmission
- Owner

### Target Variable

- Selling Price

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked the dataset information and shape.
3. Checked for missing values.
4. Converted categorical variables into numerical values using one-hot encoding.
5. Removed `Car_Name` from the features because it is a categorical identifier.
6. Selected `Selling_Price` as the target variable.
7. Split the dataset into training and testing sets using an 80:20 ratio.

## Machine Learning Model

### Linear Regression

A Linear Regression model was trained using the preprocessed dataset.

- Training samples: 240
- Testing samples: 61
- Number of features: 8

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

| Metric | Value |
|---|---:|
| MAE | 1.22 |
| RMSE | 1.87 |
| R² Score | 0.85 |

The R² score of 0.85 indicates that the model explains approximately 85% of the variation in car selling prices on the test data.

## Visualization

### Actual vs Predicted Car Prices

The following graph compares the actual selling prices with the prices predicted by the Linear Regression model.

![Actual vs Predicted Car Prices](images/actual_vs_predicted.png)

## Conclusion

This project demonstrates how machine learning can be used to predict used car prices. Data preprocessing, categorical encoding, feature selection, Linear Regression, and model evaluation were performed using Python and Scikit-learn.

The model achieved an R² score of 0.85, showing good predictive performance on the test dataset.