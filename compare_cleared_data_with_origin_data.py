import pandas as pd
import numpy as np

df1 = pd.read_excel("cleared.xlsx", sheet_name="sheet_1")
df2 = pd.read_excel("origin.xlsx", sheet_name="sheet_1")

if not df1.columns.equals(df2.columns):
    raise ValueError("Column names do not match between the two files.")

def check_value(val1, val2):
    if pd.isna(val1) and pd.isna(val2):
        return np.nan 
    if val1 != val2:
        return "Mismatch" 
    return val1

df_result = df1.copy()

for col in df1.columns:
    df_result[col] = df1[col].combine(df2[col], check_value)

df_result.to_excel("compared_result.xlsx", sheet_name="difference", index=False)
