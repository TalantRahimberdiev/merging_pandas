import pandas as pd
import numpy as np

# Read both Excel files
df1 = pd.read_excel("cleared.xlsx", sheet_name="sheet_1")
df2 = pd.read_excel("origin.xlsx", sheet_name="sheet_1")

# Ensure both DataFrames have the same columns
if not df1.columns.equals(df2.columns):
    raise ValueError("Column names do not match between the two files.")

# Function to compare numbers and ignore empty cells
def check_value(val1, val2):
    if pd.isna(val1) and pd.isna(val2):  # Ignore empty cells
        return np.nan  # Keep empty cells as NaN
    if val1 != val2:
        return "Mismatch"  # Mark mismatches
    return val1  # Keep common values

# Create a copy of df1 to store results
df_result = df1.copy()

# Apply the check_value function element-wise for each column
for col in df1.columns:
    df_result[col] = df1[col].combine(df2[col], check_value)

# Save the result to a new Excel file
df_result.to_excel("compared.xlsx", sheet_name="difference", index=False)
