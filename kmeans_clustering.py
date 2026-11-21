import pandas as pd

# Step 1: Create a dataset
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan'],
    'Age': [23, 35, 42, 28, 39],
    'Salary': [25000, 40000, 50000, 30000, 45000],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Mumbai']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Data Generalization
def generalize_age(age):
    if age < 30:
        return '20-29'
    elif age < 40:
        return '30-39'
    else:
        return '40-49'

df['Age_Group'] = df['Age'].apply(generalize_age)

print("\nGeneralized Dataset:")
print(df[['Name', 'Age_Group', 'Salary', 'City']])

# Step 3: Data Summarization
summary = df.groupby('Age_Group').agg(
    Average_Salary=('Salary', 'mean'),
    Minimum_Salary=('Salary', 'min'),
    Maximum_Salary=('Salary', 'max'),
    Count=('Name', 'count')
).reset_index()

print("\nSummarized Dataset:")
print(summary)