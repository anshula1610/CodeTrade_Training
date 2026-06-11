# AI/ML Internship Practice Assignment
## Advanced Pandas, Data Visualization & SQL Essentials

### Project Overview
This project demonstrates the use of **Pandas**, **Matplotlib**, **Seaborn**, and **SQLite** to perform end-to-end data analysis on a sample sales dataset.

The objective is to show how both **Pandas** and **SQL** can be used to answer business questions through data cleaning, analysis, visualization, and database querying.

---

## Technologies Used

- Python 3.14
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite3
- Jupyter Notebook

---

## Dataset Structure

The project uses three related tables:

### Customers Table
| Column | Description |
|----------|------------|
| customer_id | Unique customer ID |
| customer_name | Customer name |
| region | Customer region |
| segment | Customer segment |

### Products Table
| Column | Description |
|----------|------------|
| product_id | Unique product ID |
| product_name | Product name |
| category | Product category |
| price | Product price |

### Orders Table
| Column | Description |
|----------|------------|
| order_id | Unique order ID |
| customer_id | Customer reference |
| product_id | Product reference |
| quantity | Quantity ordered |
| order_date | Date of order |

---

# Tasks Completed

## Task 1: Data Audit
Performed data quality assessment including:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate records
- Unique value counts

### Outcome
Generated a complete data quality summary for all tables.

---

## Task 2: Data Cleaning

Performed:

- Column name standardization
- Missing value handling
- Data type verification
- Dataset validation

### Outcome
Created cleaned DataFrames ready for analysis.

---

## Task 3: GroupBy Analysis

Analyzed sales performance by:

- Region
- Product Category
- Customer Segment

Performed multi-level grouping using:

```python
groupby(['region', 'category'])
```

### Outcome

Business-oriented summary tables showing revenue trends.

---

## Task 4: Data Merging & KPI Calculation

Merged:

- Customers
- Orders
- Products

Calculated:

- Total Revenue
- Average Order Value
- Top Selling Products

### Revenue Formula

```python
Revenue = Quantity × Price
```

### Outcome

Created a consolidated analytical dataset.

---

## Task 5: Pivot Tables

Generated pivot tables for:

### Region vs Category

Used to compare product category performance across regions.

### Segment vs Category

Used to compare purchasing behavior of customer segments.

### Outcome

Easy-to-read business summary tables.

---

## Task 6: Data Visualization

Created six visualizations:

### 1. Histogram

Shows revenue distribution.

### 2. Scatter Plot

Shows relationship between quantity and revenue.

### 3. Bar Chart

Shows sales performance by category.

### 4. Line Chart

Shows monthly revenue trend.

### 5. Box Plot

Shows revenue spread across categories.

### 6. Heatmap

Visual comparison of regional sales performance.

### Outcome

Visual representation of business insights.

---

## Task 7: Business Insights

Key findings:

1. Electronics generated the highest revenue.
2. Revenue increased over time.
3. Larger order quantities resulted in higher revenue.
4. North region contributed significantly to sales.
5. Corporate customers generated strong revenue.
6. Heatmap revealed category-wise regional strengths.

---

## Task 8: SQLite Database & SQL Queries

Created an SQLite database:

```python
sales.db
```

Implemented 15 SQL queries covering:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- Aggregations
- JOINs
- Subqueries

### Example Query

```sql
SELECT region,
SUM(quantity)
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY region;
```

---

## Task 9: Pandas vs SQL Comparison

Replicated revenue analysis using:

### Pandas

```python
merged.groupby('region')['revenue'].sum()
```

### SQL

```sql
SELECT region,
SUM(quantity * price)
FROM ...
GROUP BY region;
```

### Comparison

| Pandas | SQL |
|----------|----------|
| Flexible for transformations | Excellent for database operations |
| Easy integration with visualization | Highly optimized for querying |
| Better for exploratory analysis | Better for large-scale data retrieval |

Both approaches produced identical business results.

---

# Project Structure

```text
project/
│
├── sales_analysis.ipynb
├── sales.db
├── README.md
│
├── customers.csv
├── products.csv
├── orders.csv
│
└── visualizations/
    ├── histogram.png
    ├── scatter_plot.png
    ├── bar_chart.png
    ├── line_chart.png
    ├── box_plot.png
    └── heatmap.png
```

---

# How to Run

### Clone Repository

```bash
git clone <repository-url>
cd project
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
sales_analysis.ipynb
```

Run all cells sequentially.

---

# Learning Outcomes

By completing this project, I gained hands-on experience in:

- Data Cleaning
- Data Analysis using Pandas
- Data Aggregation
- Pivot Tables
- Data Visualization
- SQL Query Writing
- Database Management with SQLite
- Business Insight Generation
- Comparing Pandas and SQL Workflows

---

## Author

**Anshula**
B.Tech 
Artificial Intelligence & Data Science

AI/ML Internship Practice Assignment