# Data Cleanser – Project 2

### Data Preprocessing and Feature Engineering

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter)

---

## About the Project

**Data Cleanser** is a practical Data Preprocessing and Feature Engineering project created using Python and Jupyter Notebook.

The project uses a synthetic **Patient Health Records** dataset containing missing values and extreme values. Different preprocessing techniques are applied to clean and prepare the dataset for further analysis and machine learning.

---

## Objectives

- Identify missing values.
- Calculate missing-value percentages.
- Apply different imputation techniques.
- Detect outliers using statistical methods.
- Treat extreme values using Winsorization.
- Compare data before and after cleaning.
- Generate a final cleaned dataset.

---

## Dataset

The project uses a synthetic Patient Health Records dataset.

| Column | Description |
|---|---|
| `patient_id` | Unique patient ID |
| `age` | Patient age |
| `gender` | Male / Female |
| `region` | North / South / East / West |
| `bmi` | Body Mass Index |
| `blood_pressure` | Systolic blood pressure |
| `cholesterol` | Cholesterol level |
| `glucose` | Fasting glucose level |
| `disease_risk` | 0 = Low Risk, 1 = High Risk |

> The dataset is synthetic and is created only for educational purposes.

---

## Techniques Used

### Missing Value Handling

- Mean Imputation
- Median Imputation
- Most Frequent Imputation
- Random Sample Imputation
- KNN Imputation
- MICE

### Outlier Detection

- Z-Score
- IQR Method
- Percentile Method

### Outlier Treatment

- Winsorization

---

## Project Workflow

```text
Dataset
   ↓
Data Inspection
   ↓
Missing Value Analysis
   ↓
Imputation
   ↓
Outlier Detection
   ↓
Winsorization
   ↓
Before / After Comparison
   ↓
Final Cleaned Dataset
```

---

## Project Structure

```text
Data-Cleanser/
│
├── README.md
├── Data_Cleanser_Practical.ipynb
├── requirements.txt
│
├── data/
│   ├── patient_health_records.csv
│   └── missing_value_report.csv
│
├── output/
│   ├── final_cleaned_patient_health_records.csv
│   └── outlier_comparison.csv
│
├── screenshots/
│   ├── 01_dataset_preview.png
│   ├── 02_missing_value_report.png
│   ├── 03_mean_median.png
│   ├── 04_categorical_imputation.png
│   ├── 05_knn_mice.png
│   ├── 06_zscore.png
│   ├── 07_iqr_percentile.png
│   ├── 08_winsorization.png
│   ├── 09_before_after.png
│   └── 10_final_dataset.png
│
└── docs/
    ├── Theory.md
    ├── Practical_Guide.md
    └── Dataset_Information.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Matplotlib
- Jupyter Notebook

---

## Installation

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Data_Cleanser_Practical.ipynb
```

Run the notebook cells from top to bottom.

---

## Output

The final cleaned dataset is generated at:

```text
output/final_cleaned_patient_health_records.csv
```

Screenshots of the practical steps are available in the `screenshots` folder.

---

## Learning Outcomes

Through this project, I learned how to:

- Handle missing values.
- Compare imputation methods.
- Detect and treat outliers.
- Use statistical preprocessing techniques.
- Compare datasets before and after cleaning.
- Prepare data for machine learning.

---

## Author

**Prince**  
Diploma – AI/ML & Data Science

---

> **Note:** This project is created for educational purposes and uses synthetic patient data.
