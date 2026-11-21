
import pandas as pd

# Step 1: Create a sample dataset
data = {
    "Student": ["Amit", "Priya", "Rahul", "Sneha",
                "Riya", "Karan", "Neha", "Rohan"],
    "City": ["Pune", "Mumbai", "Pune", "Nashik",
             "Mumbai", "Pune", "Nashik", "Mumbai"],
    "Age": [18, 19, 20, 21, 19, 20, 18, 21],
    "Marks": [75, 85, 90, 65, 80, 70, 95, 85],
    "Department": ["CSE", "IT", "CSE", "AIML",
                   "IT", "CSE", "AIML", "IT"]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATASET =====")
print(df.to_string(index=False))


# Step 2: Data Generalization
# Convert detailed ages into age groups

def age_group(age):
    if age <= 18:
        return "18 or below"
    elif age <= 20:
        return "19-20"
    else:
        return "21-22"

df["Age_Group"] = df["Age"].apply(age_group)

# Generalize city information into a broader region
city_region = {
    "Pune": "Western Maharashtra",
    "Mumbai": "Western Maharashtra",
    "Nashik": "Northern Maharashtra"
}

df["Region"] = df["City"].map(city_region)

print("\n===== DATA AFTER GENERALIZATION =====")
print(df[["Student", "Age_Group", "Region",
          "Department", "Marks"]].to_string(index=False))


# Step 3: Data Summarization
# Calculate overall statistics

print("\n===== OVERALL SUMMARY =====")
print("Total students:", len(df))
print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())


# Step 4: Group-wise summarization by department

print("\n===== DEPARTMENT-WISE SUMMARY =====")

summary = df.groupby("Department").agg(
    Total_Students=("Student", "count"),
    Average_Marks=("Marks", "mean"),
    Maximum_Marks=("Marks", "max"),
    Minimum_Marks=("Marks", "min")
).round(2)

print(summary)


# Step 5: Summary by generalized age group

print("\n===== AGE-GROUP-WISE SUMMARY =====")

age_summary = df.groupby("Age_Group").agg(
    Total_Students=("Student", "count"),
    Average_Marks=("Marks", "mean")
).round(2)

print(age_summary)

print("\nData generalization and summarization completed.")
