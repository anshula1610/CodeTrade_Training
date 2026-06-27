# 📊 Phase 2 Mini Project – E-Commerce Data Analysis & Machine Learning

## 📌 Project Overview

This project performs an end-to-end analysis of the Brazilian Olist E-Commerce dataset. It includes data preprocessing, exploratory data analysis (EDA), SQL-based business insights, machine learning model development, model evaluation, and explainable AI using SHAP.

The notebook demonstrates the complete data science workflow—from raw data to business insights and predictive modeling.

---

## 🎯 Objectives

- Clean and preprocess multiple e-commerce datasets.
- Perform exploratory data analysis (EDA).
- Merge datasets for comprehensive analysis.
- Generate business insights using SQL.
- Build and evaluate a machine learning classification model.
- Interpret predictions using SHAP explainability.

---

## 📂 Dataset

The project uses the **Olist Brazilian E-Commerce Dataset** containing information about:

- Orders
- Customers
- Order Payments
- Order Items
- Products

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite3
- Scikit-learn
- XGBoost
- SHAP
- Jupyter Notebook

---

## 📋 Project Workflow

### Task 1 – Data Preprocessing & Exploratory Data Analysis

- Loaded multiple CSV datasets
- Checked data shapes and information
- Identified missing values
- Removed duplicate records
- Converted timestamp columns to datetime format
- Merged datasets into a single dataframe
- Performed exploratory data analysis
- Generated visualizations
- Derived key business insights

---

### Task 2 – SQL Business Analysis

Using SQLite, business-related queries were executed to analyze:

- Customer purchasing behavior
- Order statistics
- Payment information
- Product-related insights

SQL was used to transform and analyze the cleaned dataset efficiently.

---

### Task 3 – Machine Learning Model Preparation

- Selected features and target variable
- Performed train-test split
- Applied preprocessing pipeline
- Encoded categorical variables
- Scaled numerical features
- Selected evaluation metrics

---

### Task 4 – Model Training

Implemented an **XGBoost Classification Model**.

Model development included:

- Data preprocessing pipeline
- Model training
- Prediction on test data
- Performance evaluation

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

### Task 5 – Explainable AI (SHAP)

To improve model interpretability:

- SHAP values were calculated
- Individual predictions were explained
- Feature contributions were visualized
- Waterfall plots were generated

This helps understand how each feature influences model predictions.

---

## 📊 Key Insights

Some important observations from the analysis include:

- Most orders are delivered within a limited delivery-time range.
- Customer purchasing patterns can be identified from transaction history.
- SQL queries provide useful business intelligence from the cleaned dataset.
- XGBoost provides strong predictive performance.
- SHAP improves transparency by explaining individual model decisions.

---

## 📁 Project Structure

```
Phase2_mini_project.ipynb
README.md
olist_orders_dataset.csv
olist_customers_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_products_dataset.csv
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone <repository-url>
```

2. Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap
```

3. Place all dataset CSV files in the project directory.

4. Open the notebook.

```bash
jupyter notebook Phase2_mini_project.ipynb
```

5. Run all cells sequentially.

---

## 📈 Results

- Successfully cleaned and merged multiple datasets.
- Generated business insights through EDA and SQL.
- Built an XGBoost classification model.
- Evaluated model performance using standard classification metrics.
- Explained model predictions using SHAP for better interpretability.

---

## 🚀 Future Improvements

- Hyperparameter tuning for improved performance.
- Deployment using Flask or FastAPI.
- Interactive dashboard using Streamlit or Power BI.
- Automated data pipeline.
- Model monitoring and retraining pipeline.

---

## 👩‍💻 Author

**Anshula**

B.Tech – Artificial Intelligence & Data Science

---

## 📄 License

This project is developed for educational and learning purposes.