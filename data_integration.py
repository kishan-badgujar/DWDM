import pandas as pd

# Read data from CSV files
student_details = pd.read_csv("student_details.csv")
student_marks = pd.read_csv("student_marks.csv")

# Integrate the two datasets using Student_ID
integrated_data = pd.merge(
    student_details,
    student_marks,
    on="Student_ID"
)

# Display the integrated data
print("Integrated Student Data:")
print(integrated_data)

# Save integrated data into a new CSV file
integrated_data.to_csv("integrated_students.csv", index=False)

print("\nData integration completed successfully!")
