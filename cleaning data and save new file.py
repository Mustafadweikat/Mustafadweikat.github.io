import pandas as pd
import os

# read file
df = pd.read_csv(
    r"F:\Career development program\Practice\Agricultural project\spss-e\crop1.csv",
    encoding="utf-8-sig",
    low_memory=False
)
  

print("========== BEFORE CLEANING ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# delet complitly empty rows only
empty_rows_before = df.shape[0]
df = df.dropna(how='all')
empty_rows_removed = empty_rows_before - df.shape[0]

# delet complitly empty columns only
empty_cols_before = df.shape[1]
df = df.dropna(axis=1, how='all')
empty_cols_removed = empty_cols_before - df.shape[1]

# delet frequncy columns
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

print("\n========== CLEANING REPORT ==========")
print("Empty rows removed:", empty_rows_removed)
print("Empty columns removed:", empty_cols_removed)
print("Duplicated rows removed:", duplicates_removed)

print("\n========== AFTER CLEANING ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# save file
df.to_csv("agriculture_cleaned.csv", index=False)

print("\nFile saved successfully.")
print("Saved in:", os.getcwd())
