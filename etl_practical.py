
import sqlite3
import pandas as pd

# 1. EXTRACT: Create sample source data
data = {
    "student_id": [1, 2, 3, 4, 5],
    "student_name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "department": ["Computer", "IT", "Computer", "IT", "ENTC"],
    "marks": [85, 90, 70, 95, 60]
}

source_df = pd.DataFrame(data)

print("EXTRACTED DATA:")
print(source_df)

# 2. TRANSFORM: Clean and process the data
transformed_df = source_df.copy()

transformed_df["student_name"] = transformed_df["student_name"].str.upper()
transformed_df["department"] = transformed_df["department"].str.upper()

transformed_df["result"] = transformed_df["marks"].apply(
    lambda marks: "PASS" if marks >= 40 else "FAIL"
)

print("\nTRANSFORMED DATA:")
print(transformed_df)

# 3. LOAD: Store transformed data in SQLite database
connection = sqlite3.connect("etl_practical.db")

transformed_df.to_sql(
    "target_students",
    connection,
    if_exists="replace",
    index=False
)

# Verify the loaded data
loaded_df = pd.read_sql_query(
    "SELECT * FROM target_students",
    connection
)

print("\nLOADED DATA:")
print(loaded_df)

connection.close()

print("\nETL PROCESS COMPLETED SUCCESSFULLY!")
