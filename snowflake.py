# Practical 2: Multidimensional Data Model (Snowflake Schema)

# Product Dimension
product = {
    101: {"name": "Laptop", "category_id": 1},
    102: {"name": "Mobile", "category_id": 2},
    103: {"name": "Tablet", "category_id": 2}
}

# Category Dimension
category = {
    1: "Computer",
    2: "Electronics"
}

# Customer Dimension
customer = {
    1: {"name": "Mamta", "city_id": 1},
    2: {"name": "Rahul", "city_id": 2},
    3: {"name": "Priya", "city_id": 3}
}

# City Dimension
city = {
    1: {"city": "Akola", "state_id": 1},
    2: {"city": "Pune", "state_id": 1},
    3: {"city": "Mumbai", "state_id": 2}
}

# State Dimension
state = {
    1: "Maharashtra",
    2: "Maharashtra"
}

# Sales Fact Table
sales = [
    {
        "Customer_ID": 1,
        "Product_ID": 101,
        "Quantity": 2,
        "Sales_Amount": 100000
    },
    {
        "Customer_ID": 2,
        "Product_ID": 102,
        "Quantity": 3,
        "Sales_Amount": 60000
    },
    {
        "Customer_ID": 3,
        "Product_ID": 103,
        "Quantity": 1,
        "Sales_Amount": 30000
    }
]

# Display Snowflake Data Model

print("========== SNOWFLAKE DATA MODEL ==========")

print("\nProduct Dimension:")
for key, value in product.items():
    print(key, ":", value)

print("\nCategory Dimension:")
for key, value in category.items():
    print(key, ":", value)

print("\nCustomer Dimension:")
for key, value in customer.items():
    print(key, ":", value)

print("\nCity Dimension:")
for key, value in city.items():
    print(key, ":", value)

print("\nState Dimension:")
for key, value in state.items():
    print(key, ":", value)

print("\nSales Fact Table:")
for record in sales:
    print(record)

print("\n========== SNOWFLAKE MODEL CREATED SUCCESSFULLY ==========")