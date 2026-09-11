import pandas as pd
import sqlite3

def read_customer_csv(file_name):
    return pd.read_csv(file_name)

def read_customer_json(file_name):
    return pd.read_json(file_name)

def read_customer_database(file_name):
    con = sqlite3.connect(file_name)
    try:
        return pd.read_sql_query("SELECT * FROM customers", con)
    finally:
        con.close()

def clean_data(data):
    data = data.copy()
    data["Age"] = data["Age"].fillna(data["Age"].median())
    data["Income"] = data["Income"].fillna(data["Income"].median())
    data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
    return data.drop_duplicates()
