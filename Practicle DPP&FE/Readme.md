# Data Preprocessing & Feature Engineering

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-Numerical-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-Preprocessing-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">

</p>

<p align="center">

<img src="https://img.shields.io/badge/Data%20Cleaning-Completed-2EA44F?style=for-the-badge">
<img src="https://img.shields.io/badge/Feature%20Engineering-Completed-2EA44F?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-0A66C2?style=for-the-badge">
<img src="https://img.shields.io/badge/Verified-✓-2EA44F?style=for-the-badge">

</p>

---

## 📌 Project Overview

A practical **Data Preprocessing and Feature Engineering** project covering the topics taught in the course from data analysis and data cleaning through feature transformation and construction.

The project uses practical Python implementations for working with structured data, missing values, outliers, categorical variables, numerical features, scaling and transformations.

---

## 🎯 Objectives

- Load data from CSV, Excel, JSON and SQL sources
- Fetch data from an API
- Understand and clean datasets
- Perform exploratory data analysis
- Handle missing values
- Detect and treat outliers
- Handle date/time and mixed variables
- Encode categorical variables
- Encode numerical features
- Apply feature scaling
- Construct and transform features
- Use `FunctionTransformer`
- Use `PowerTransformer`
- Apply `ColumnTransformer`
- Export the final processed dataset

---

## 📚 Course Topics Covered

### 1. Data Analysis
- Data Analysis
- Data Science Project Planning
- Framing a Machine Learning Problem
- Tensors
- Tensor in-depth concepts

### 2. Working With Data
- CSV files
- JSON
- SQL
- API data
- Data understanding
- Data cleaning

### 3. Exploratory Data Analysis
- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Pandas Profiling

### 4. Missing Value Imputation
- Simple Imputer
- Numerical missing-value handling
- Categorical missing-value handling
- Most Frequent Imputation
- Missing Indicator
- Random Sample Imputation
- KNN Imputer
- MICE

### 5. Outlier Handling
- Z-score
- IQR
- Percentile Method
- Winsorization

### 6. Feature Transformation & Construction
- Mixed Variables
- Date and Time Variables
- Complete Case Analysis
- Ordinal Encoding
- Label Encoding
- One-Hot Encoding
- Binning / Discretization
- Binarization
- Quantile Binning
- K-Means Binning
- Standardization
- Normalization
- MinMax Scaling
- MaxAbs Scaling
- Robust Scaling
- Feature Construction & Splitting
- Log Transformation
- Reciprocal Transformation
- Square Root Transformation
- Box-Cox Transformation
- Yeo-Johnson Transformation
- Column Transformer

---

## 🛠️ Technologies

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square">
<img src="https://img.shields.io/badge/Seaborn-76B900?style=flat-square">
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white">

</p>

---

## 📂 Project Structure

```text
Practicle DPP&FE/
│
├── Dataset/
│   ├── customers.xlsx
│   ├── transactions.json
│   └── products.sql
│
├── Notebook/
│   ├── DataPreprocessing.ipynb
│   └── DataPreprocessing_Updated.ipynb
│
├── Final Dataset/
│   └── processed_customer_data.csv
│
├── Screenshots/
│   ├── 01_data_import.png
│   ├── 02_eda_correlation.png
│   ├── 03_missing_data.png
│   ├── 04_outliers.png
│   ├── 05_scaling.png
│   └── 06_final_validation.png
│
├── requirements.txt
├── Summary_Report.md
└── README.md
```

---

## 🔄 Workflow

```text
Data Sources
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
EDA
     ↓
Missing Value Handling
     ↓
Outlier Detection
     ↓
Encoding
     ↓
Numerical Feature Encoding
     ↓
Feature Scaling
     ↓
Feature Construction
     ↓
Feature Transformation
     ↓
ColumnTransformer
     ↓
Final Validation
     ↓
Processed CSV
```

---

## 📊 Practical Implementation

### Data Import
Excel, JSON, SQL and API data are loaded and inspected using Python.

### EDA
The project performs univariate, bivariate and multivariate analysis using Pandas, Matplotlib and Seaborn.

### Missing Values
Different imputation approaches from the syllabus are implemented and compared where applicable.

### Outliers
Z-score, IQR, percentile and Winsorization techniques are demonstrated.

### Encoding
Categorical and numerical feature encoding techniques from the syllabus are implemented.

### Scaling
Standardization, normalization, MinMax, MaxAbs and Robust scaling are demonstrated.

### Transformation
`FunctionTransformer` is used for log, reciprocal and square-root transformations. `PowerTransformer` is used for Box-Cox and Yeo-Johnson transformations.

---

## 🖼️ Screenshots

### Data Import
![Data Import](Screenshots/01_data_import.png)

### EDA
![EDA](Screenshots/02_eda_correlation.png)

### Missing Values
![Missing Values](Screenshots/03_missing_data.png)

### Outliers
![Outliers](Screenshots/04_outliers.png)

### Feature Scaling
![Scaling](Screenshots/05_scaling.png)

### Final Validation
![Final Validation](Screenshots/06_final_validation.png)

---

## ⚙️ Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

For Python 3.14:

```bash
py -3.14 -m pip install -r requirements.txt
```

---

## ▶️ Run the Project

1. Open the project folder in VS Code.
2. Open `Notebook/DataPreprocessing_Updated.ipynb`.
3. Select the Python environment where the requirements are installed.
4. Run the notebook from top to bottom.
5. Check the processed dataset in `Final Dataset/`.

---

## 📤 Output

The final processed dataset is:

```text
Final Dataset/processed_customer_data.csv
```

---

## ✅ Project Status

<p align="center">

<img src="https://img.shields.io/badge/Project-Completed-2EA44F?style=for-the-badge">
<img src="https://img.shields.io/badge/Notebook-Verified-2EA44F?style=for-the-badge">
<img src="https://img.shields.io/badge/Output-Generated-2EA44F?style=for-the-badge">

</p>

---

## 👨‍💻 Project

**Data Preprocessing & Feature Engineering Practical**

Built as a course practical covering the taught data analysis, data cleaning, and feature transformation topics.
