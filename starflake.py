# Practical 1: Multidimensional Data Model (Starflake)

# Dimension Table: Customer
customer = {
    1: "Mamta",
    2: "Rahul",
    3: "Priya"
}

# Dimension Table: Product
product = {
    101: "Laptop",
    102: "Mobile",
    103: "Tablet"
}

# Dimension Table: Time
time = {
    1: "2026-09-27",
    2: "2026-09-28",
    3: "2026-09-29"
}

# Dimension Table: Location
location = {
    1: "Akola",
    2: "Pune",
    3: "Mumbai"
}

# Fact Table: Sales
sales = [
    {
        "Customer_ID": 1,
        "Product_ID": 101,
        "Time_ID": 1,
        "Location_ID": 1,
        "Quantity": 2,
        "Sales_Amount": 100000
    },
    {
        "Customer_ID": 2,
        "Product_ID": 102,
        "Time_ID": 2,
        "Location_ID": 2,
        "Quantity": 3,
        "Sales_Amount": 60000
    },
    {
        "Customer_ID": 3,
        "Product_ID": 103,
        "Time_ID": 3,
        "Location_ID": 3,
        "Quantity": 1,
        "Sales_Amount": 30000
    }
]

# Display the Starflake Data Model

print("========== STARFLAKE DATA MODEL ==========")

print("\nCustomer Dimension:")
for key, value in customer.items():
    print(key, ":", value)

print("\nProduct Dimension:")
for key, value in product.items():
    print(key, ":", value)

print("\nTime Dimension:")
for key, value in time.items():
    print(key, ":", value)

print("\nLocation Dimension:")
for key, value in location.items():
    print(key, ":", value)

print("\nSales Fact Table:")
for record in sales:
    print(record)

print("\n========== MODEL CREATED SUCCESSFULLY ==========")