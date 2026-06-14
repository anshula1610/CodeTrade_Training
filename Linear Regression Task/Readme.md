# California Housing Price Prediction using Linear Regression

## Project Overview

This project is part of the AI/ML Internship Program and focuses on implementing and evaluating Linear Regression models using the California Housing dataset.

The objective is to predict house prices based on various housing and demographic features while exploring model performance through different evaluation metrics and experimental setups.

---

## Dataset

**Dataset:** California Housing Prices

The dataset contains information collected from the California census, including housing characteristics, location information, and median house values.

### Target Variable

* `median_house_value`

### Example Features

* longitude
* latitude
* housing_median_age
* total_rooms
* total_bedrooms
* population
* households
* median_income
* ocean_proximity

---

## Project Tasks

### Task 1: Baseline Linear Regression Model

* Loaded and preprocessed the dataset.
* Handled missing values.
* Applied one-hot encoding to categorical features.
* Split the data into training and testing sets.
* Trained a Linear Regression model.
* Generated predictions on the test dataset.
* Evaluated performance using:

  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * Mean Absolute Error (MAE)
  * R² Score
* Compared actual and predicted values.
* Visualized actual vs predicted house prices.

---

### Task 2: One-Feature vs Multi-Feature Models

#### Model A

Used only:

* median_income

#### Model B

Used:

* median_income
* housing_median_age
* total_rooms

Both models were evaluated using:

* MSE
* RMSE
* MAE
* R² Score

A comparison table was created to determine which model performs better on the test dataset.

---

### Task 3: Train-Test Split Analysis

The same Linear Regression model was tested using:

* 80/20 split
* 70/30 split
* 60/40 split

For each split:

* Training metrics were recorded.
* Testing metrics were recorded.
* Train-test gaps were analyzed.
* Model stability was examined.

A comparison chart was created to visualize performance changes across different splits.

---

### Task 4: Metric Verification and Exploration

The best-performing model was selected and evaluated further.

Activities included:

* Manual calculation of:

  * MSE
  * RMSE
  * MAE
  * R² Score

* Comparison with Scikit-Learn metric outputs.

* Additional metric:

  * Median Absolute Error

* Artificially introducing large prediction errors.

* Observing how:

  * MSE
  * RMSE
  * MAE

  react to outliers and large errors.

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## Installation

Install the required packages:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## Project Structure

```text
California_Housing_Linear_Regression/
│
├── housing.csv
├── California_Housing_Linear_Regression.ipynb
├── README.md
```

---

## Evaluation Metrics

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Square root of MSE and provides error in original units.

### Mean Absolute Error (MAE)

Measures the average absolute prediction error.

### R² Score

Indicates how well the model explains the variance in the target variable.

### Median Absolute Error

Measures the median of absolute prediction errors and is less sensitive to outliers.

---

## Results Summary

* Multi-feature Linear Regression performed better than single-feature Linear Regression.
* Median income was found to be one of the strongest predictors of house prices.
* Different train-test splits produced slightly different results, but the model remained relatively stable.
* MSE and RMSE were highly sensitive to large prediction errors, while MAE was more robust.

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Data preprocessing
* Handling missing values
* Feature engineering
* Linear Regression
* Model evaluation
* Train-test splitting
* Error metrics
* Model comparison
* Outlier impact analysis

---

## Author

Anshula

