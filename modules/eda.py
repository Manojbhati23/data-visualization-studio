import pandas as pd


def data_summary(df):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isnull().sum().sum()
    }


def statistics(df):
    return df.describe()


def missing_values(df):
    return df.isnull().sum()


def data_types(df):
    return df.dtypes