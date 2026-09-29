# 📊 PR Final — Holistic Data Preparer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge)

### Data Analysis & Data Preprocessing Practical Project

</div>

---

## 📌 Overview

**PR Final — Holistic Data Preparer** is an academic data-preprocessing project focused on preparing a customer credit-risk dataset for data analysis and machine-learning applications.

The project follows a structured workflow from raw data acquisition to final dataset validation. It demonstrates commonly used techniques for understanding, cleaning, transforming and preparing data using Python.

---

## 🎯 Objectives

- Understand the structure and quality of customer credit-risk data.
- Load data from CSV, JSON and SQLite sources.
- Perform exploratory data analysis.
- Identify and handle missing values.
- Detect and treat outliers.
- Apply encoding and binning techniques.
- Apply different numerical scaling methods.
- Perform feature transformations.
- Extract useful information from date variables.
- Construct additional features.
- Validate and export the final processed dataset.

---

## 🗂️ Dataset

The main dataset contains customer credit-risk information including demographic, employment, financial and behavioral attributes.

### Main Fields

| Field | Description |
|---|---|
| `customer_id` | Unique customer identifier |
| `age` | Customer age |
| `gender` | Gender category |
| `region` | Customer region |
| `education_level` | Education category |
| `employment_type` | Employment category |
| `annual_income` | Annual income |
| `loan_amount` | Loan amount |
| `loan_purpose` | Purpose of the loan |
| `credit_score` | Customer credit score |
| `repayment_history` | Repayment history |
| `transaction_count` | Number of transactions |
| `spending_ratio` | Spending ratio |
| `join_date` | Customer joining date |
| `default_flag` | Default indicator |

Supporting JSON and SQLite files are included to demonstrate multiple data-acquisition methods.

---

## 🔄 Project Workflow

```text
Data Acquisition
       ↓
Data Understanding
       ↓
Exploratory Data Analysis
       ↓
Data Cleaning
       ↓
Missing-Value Treatment
       ↓
Outlier Detection
       ↓
Feature Transformation
       ↓
Encoding & Binning
       ↓
Feature Scaling
       ↓
Feature Construction
       ↓
Final Validation
       ↓
Clean / Analysis-Ready Dataset
```

---

## 📥 1. Data Acquisition

The practical demonstrates working with different data sources:

- CSV dataset
- JSON data
- SQLite database
- API concept

The main customer dataset is loaded from CSV, while JSON and SQLite files provide supporting data for the practical.

---

## 🔎 2. Data Understanding

The raw data is inspected before preprocessing using:

- Dataset preview
- Shape and dimensions
- Column names
- Data types
- Descriptive statistics
- Missing-value checks
- Duplicate checks

This helps identify the structure and initial quality of the dataset.

---

## 📊 3. Exploratory Data Analysis

EDA is used to understand distributions, relationships and patterns in the customer data.

### Covered Analysis

- Univariate analysis
- Bivariate analysis
- Multivariate analysis
- Statistical summaries
- Data visualization

---

## 🧹 4. Data Cleaning

The cleaning stage prepares the raw data for further analysis.

### Missing-Value Techniques

- SimpleImputer
- Mean imputation
- Most-frequent imputation
- Missing indicators
- Random-sample imputation
- KNN Imputer
- Iterative / MICE-style imputation
- Complete-case analysis

Duplicate records and missing values are also checked during validation.

---

## 🚨 5. Outlier Detection

The practical demonstrates multiple approaches for identifying unusual numerical observations:

- Z-score
- IQR method
- Percentile method
- Winsorization

These techniques help examine extreme values before further processing.

---

## 🔤 6. Encoding & Binning

Categorical and numerical variables are transformed into suitable representations.

### Encoding

- Ordinal Encoding
- Label Encoding
- One-Hot Encoding

### Binning / Discretization

- Equal-width binning
- Quantile binning
- Binarization
- K-Means based binning

---

## ⚖️ 7. Feature Scaling

Different scaling methods are demonstrated using Scikit-learn:

- StandardScaler
- Normalizer
- MinMaxScaler
- MaxAbsScaler
- RobustScaler

The techniques show how numerical features can be transformed to suitable scales.

---

## 🔄 8. Feature Transformation

The notebook demonstrates common numerical transformations:

- Log transformation
- Square-root transformation
- Reciprocal transformation
- Power transformation
- Box-Cox transformation
- Yeo-Johnson transformation
- FunctionTransformer
- PowerTransformer

---

## 📅 9. Date & Feature Construction

The `join_date` field is used to extract useful date-based information.

Additional derived features are also constructed from the available customer information, including:

- Debt-to-income related features
- Average monthly transaction features
- Spending-to-income related features
- Date-derived features

---

## 🛠️ 10. ColumnTransformer

`ColumnTransformer` is used to organize preprocessing operations for different groups of columns.

This provides a structured approach for applying different transformations to numerical and categorical features.

---

## ✅ 11. Final Validation

Before exporting the final dataset, the notebook checks:

- Dataset shape
- Missing values
- Duplicate records
- Column structure
- Final data availability

The processed dataset is then saved in the `Final Dataset` folder.

---

## 📈 Output

The final processed dataset is available at:

```text
Final Dataset/final_customer_credit_risk.csv
```

The output is prepared for further data analysis and potential machine-learning applications.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming |
| **Pandas** | Data analysis and cleaning |
| **NumPy** | Numerical operations |
| **Matplotlib** | Visualization |
| **Seaborn** | Statistical visualization |
| **Scikit-learn** | Preprocessing and transformation |
| **Jupyter Notebook** | Practical implementation |

---

## 📁 Project Structure

```text
PR_Final_Holistic_Data_Preparer/
│
├── Dataset/
│   ├── customer_credit_risk.csv
│   ├── customer_manager.json
│   └── loan_repayment.db
│
├── Final Dataset/
│   └── final_customer_credit_risk.csv
│
├── Notebook/
│   └── PR_Final_Data_Preprocessing.ipynb
│
├── Theory/
│   ├── PR_Final_Complete_Theory.md
│   └── Quick_Revision.md
│
├── Screenshots/
│   ├── 01_data_understanding.png
│   ├── 02_eda.png
│   ├── 03_missing_values.png
│   ├── 04_outliers.png
│   ├── 05_scaling.png
│   └── 06_final_validation.png
│
├── Documentation/
│   └── Summary_Report.md
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Open Jupyter Notebook

```bash
jupyter notebook
```

### 3. Open the Practical

```text
Notebook/PR_Final_Data_Preprocessing.ipynb
```

Run the notebook cells from top to bottom.

---

## 📷 Screenshots

The project includes screenshots covering:

- Data Understanding
- EDA
- Missing Values
- Outlier Detection
- Scaling
- Final Validation

These provide a visual record of the practical execution.

---

## 📚 Theory & Revision

The `Theory` folder contains concise explanations and revision material related to the practical topics.

It can be used for:

- Practical-file preparation
- Viva revision
- Topic understanding
- Quick reference before submission

---

## 🎓 Academic Scope

This project covers important concepts from **Data Analysis and Data Preprocessing**, including:

- Data acquisition
- Data understanding
- EDA
- Missing-value imputation
- Outlier handling
- Encoding
- Binning
- Scaling
- Feature transformation
- Feature construction
- Data validation

The final workflow demonstrates how raw customer data can be converted into a cleaner and more analysis-ready dataset.

---

## 👨‍💻 Author

**Prince Vaghasiya**

**Project:** PR Final — Holistic Data Preparer  
**Domain:** Data Analysis & Data Preprocessing  
**Environment:** Jupyter Notebook  
**Status:** Completed

---

<div align="center">

**Raw Data → Clean Data → Analysis-Ready Dataset**

### Made by Prince Vaghasiya

</div>
