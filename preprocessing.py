# Practical 3: Data Pre-processing Techniques

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Creating sample data
data = {
    "Name": ["Mamta", "Rahul", "Priya", "Amit", "Amit"],
    "Age": [20, 21, None, 22, 22],
    "Gender": ["Female", "Male", "Female", "Male", "Male"],
    "Marks": [85, 78, 90, 88, 88]
}

df = pd.DataFrame(data)

print("========== ORIGINAL DATA ==========")
print(df)

# 1. Handling Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# 2. Removing Duplicate Records
df = df.drop_duplicates()

# 3. Encoding Categorical Data
encoder = LabelEncoder()
df["Gender"] = encoder.fit_transform(df["Gender"])

# 4. Feature Scaling
scaler = StandardScaler()
df[["Age", "Marks"]] = scaler.fit_transform(df[["Age", "Marks"]])

print("\n========== PRE-PROCESSED DATA ==========")
print(df)

print("\n========== DATA PRE-PROCESSING COMPLETED ==========")