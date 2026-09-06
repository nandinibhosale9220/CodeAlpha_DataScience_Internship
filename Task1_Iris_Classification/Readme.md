# Task 1: Iris Flower Classification

## Objective

The objective of this project is to classify Iris flowers into three species:

- Setosa
- Versicolor
- Virginica

The classification is performed using the measurements of the flowers.

## Dataset

The Iris dataset from Scikit-learn is used.

It contains four features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The dataset contains 150 samples belonging to three species.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Machine Learning Algorithm

Logistic Regression is used for classification.

## Steps Performed

1. Loaded the Iris dataset.
2. Converted the dataset into a Pandas DataFrame.
3. Split the dataset into training and testing sets.
4. Trained a Logistic Regression model.
5. Predicted the classes of test samples.
6. Evaluated the model using accuracy and classification report.
7. Generated a confusion matrix.
8. Generated an Iris pair plot.

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Visualizations

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

### Iris Pair Plot

![Iris Pair Plot](images/iris_pairplot.png)

## Conclusion

The Logistic Regression model successfully classifies Iris flowers into their respective species using their physical measurements. This project demonstrates the basic workflow of a supervised machine learning classification problem.