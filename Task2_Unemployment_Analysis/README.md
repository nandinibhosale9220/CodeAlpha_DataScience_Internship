# Task 2: Unemployment Analysis

## Objective

Analyze unemployment trends in India using data analysis and visualization techniques. 
The project also studies the impact of COVID-19 on unemployment and identifies 
regional unemployment patterns.

## Dataset

Dataset: Unemployment in India

The dataset contains information about:
- Region
- Date
- Frequency
- Estimated Unemployment Rate (%)
- Estimated Employed
- Estimated Labour Participation Rate (%)
- Area

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Cleaned column names by removing extra spaces.
3. Checked for missing values.
4. Removed rows containing missing values.
5. Converted the Date column into datetime format.
6. Sorted the data by date.

## Analysis Performed

### 1. Overall Unemployment Trend

The unemployment rate was analyzed over time to identify major changes and trends.

![Unemployment Rate Trend](images/unemployment_rate_trend.png)

### 2. COVID-19 Impact

The unemployment rate before and during the COVID-19 period was compared to understand 
the effect of the pandemic on employment.

![COVID-19 Impact](images/covid19_unemployment_impact.png)

### 3. Region-wise Unemployment

The average unemployment rate was calculated for different regions to identify 
regional differences.

![Region-wise Unemployment](images/region_wise_unemployment.png)

## Key Insights

- The unemployment rate changed significantly over the analyzed period.
- A major increase in unemployment was observed during the COVID-19 period.
- Unemployment rates varied across different regions.
- Data visualization helps identify important unemployment trends and patterns.

## Conclusion

This project demonstrates how Python-based data analysis and visualization can be used 
to understand unemployment trends and the impact of major events such as COVID-19.