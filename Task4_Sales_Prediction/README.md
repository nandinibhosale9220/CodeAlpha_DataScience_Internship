# Task 4: Sales Prediction Using Python

## Objective

Predict product sales based on advertising expenditure on TV, Radio, and Newspaper using a machine learning regression model.

The project also analyzes how different advertising channels affect sales and provides insights for marketing decisions.

## Dataset

Dataset: Advertising.csv

The dataset contains 200 records and the following columns:

- TV - Advertising expenditure on TV
- Radio - Advertising expenditure on Radio
- Newspaper - Advertising expenditure on Newspaper
- Sales - Target variable

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Data Preprocessing

The following steps were performed:

1. Loaded the dataset using Pandas.
2. Checked the dataset information.
3. Checked for missing values.
4. Removed the unnecessary index column.
5. Selected TV, Radio, and Newspaper as input features.
6. Selected Sales as the target variable.
7. Split the dataset into training and testing sets using an 80:20 ratio.

## Machine Learning Model

### Linear Regression

A Linear Regression model was used to predict sales based on advertising expenditure.

Training data: 80%

Testing data: 20%

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

| Metric | Value |
|---|---:|
| MAE | 1.46 |
| RMSE | 1.78 |
| R² Score | 0.90 |

The R² score of 0.90 indicates that the model explains approximately 90% of the variation in sales on the test data.

## Advertising Impact

The Linear Regression coefficients were:

| Advertising Channel | Coefficient |
|---|---:|
| TV | 0.045 |
| Radio | 0.189 |
| Newspaper | 0.003 |

Radio has the largest coefficient among the three advertising channels in this model, while Newspaper has the smallest coefficient.

## Visualizations

### Actual vs Predicted Sales

![Actual vs Predicted Sales](actual_vs_predicted_sales.png)

### Advertising Correlation

![Advertising Correlation](advertising_correlation.png)

## Key Insights

- Advertising expenditure is related to product sales.
- Radio has the strongest estimated linear relationship with sales among the three advertising channels in this model.
- TV also contributes substantially to predicted sales.
- Newspaper has a comparatively smaller coefficient.
- The model achieved an R² score of 0.90, indicating good predictive performance.

## Conclusion

This project demonstrates how machine learning can be used for sales prediction using advertising expenditure. Linear Regression was applied after preprocessing the dataset, and the model achieved an R² score of 0.90.

The analysis can help businesses understand the relationship between advertising expenditure and sales and support data-driven marketing decisions.