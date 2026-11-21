import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Read the transaction data
data = pd.read_csv("transactions.csv")

# Convert items into lists
transactions = data["Items"].apply(lambda x: x.split()).tolist()

# Convert transactions into True/False format
te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)

df = pd.DataFrame(te_data, columns=te.columns_)

# Apply Apriori algorithm
frequent_itemsets = apriori(
    df,
    min_support=0.25,
    use_colnames=True
)

# Generate association rules
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.5
)

# Display frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Display association rules
print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support", "confidence"]])