
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Create transaction dataset
transactions = [
    ["Bread", "Milk"],
    ["Bread", "Diaper", "Beer", "Eggs"],
    ["Milk", "Diaper", "Beer", "Coke"],
    ["Bread", "Milk", "Diaper", "Beer"],
    ["Bread", "Milk", "Diaper", "Coke"],
    ["Bread", "Eggs"],
    ["Milk", "Diaper", "Beer"],
    ["Bread", "Milk", "Diaper", "Beer"]
]

print("===== TRANSACTION DATASET =====")
for i, transaction in enumerate(transactions, start=1):
    print(f"Transaction {i}: {transaction}")

# Step 2: Convert transactions into a Boolean table
encoder = TransactionEncoder()
encoded_data = encoder.fit(transactions).transform(transactions)

df = pd.DataFrame(
    encoded_data,
    columns=encoder.columns_
)

print("\n===== ENCODED TRANSACTION DATA =====")
print(df.astype(int).to_string(index=False))

# Step 3: Find frequent itemsets using Apriori
frequent_itemsets = apriori(
    df,
    min_support=0.25,
    use_colnames=True
)

print("\n===== FREQUENT ITEMSETS =====")
print(frequent_itemsets.to_string(index=False))

# Step 4: Extract association rules
if not frequent_itemsets.empty:
    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=0.60
    )

    print("\n===== ASSOCIATION RULES =====")

    if not rules.empty:
        result = rules[
            ["antecedents", "consequents",
             "support", "confidence", "lift"]
        ].copy()

        result["antecedents"] = result["antecedents"].apply(
            lambda x: ", ".join(sorted(x))
        )
        result["consequents"] = result["consequents"].apply(
            lambda x: ", ".join(sorted(x))
        )

        print(result.round(2).to_string(index=False))
    else:
        print("No rules satisfy the minimum confidence.")
else:
    print("No frequent itemsets found.")

print("\nAssociation rule mining completed successfully!")
