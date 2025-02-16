import pandas as pd

# Read the cleared data
cleared = pd.read_excel("cleared.xlsx", sheet_name='sheet_1')

# Read and group data from tmp.xlsx
tmp_sheet_1 = pd.read_excel("tmp.xlsx", sheet_name='sheet_1').groupby('atm_id', as_index=False)['count_a'].sum()
tmp_sheet_2 = pd.read_excel("tmp.xlsx", sheet_name='sheet_2').groupby('atm_id', as_index=False)['count_b'].sum()
tmp_sheet_3 = pd.read_excel("tmp.xlsx", sheet_name='sheet_3').groupby('atm_id', as_index=False)['count_c'].sum()

# Perform left joins
merged_df = cleared.merge(tmp_sheet_1, on="atm_id", how="left")
merged_df = merged_df.merge(tmp_sheet_2, on="atm_id", how="left")
merged_df = merged_df.merge(tmp_sheet_3, on="atm_id", how="left")

# Print the final merged DataFrame
print(merged_df)

# Save the merged DataFrame to a new Excel file
merged_df.to_excel("cleared.xlsx", sheet_name="sheet_1", index=False)

