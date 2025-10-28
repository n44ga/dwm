transactions = [
    ['I1', 'I2', 'I5'], ['I2', 'I4'], ['I2', 'I3'], ['I1', 'I2', 'I4'],
    ['I1', 'I3'], ['I2', 'I3'], ['I1', 'I3'], ['I1', 'I2', 'I3', 'I5'],
    ['I1', 'I2', 'I3']
]
total_transactions = len(transactions)

antecedent = ['I1', 'I3']  # The "IF" part
consequent = ['I2']      # The "THEN" part

full_itemset = list(set(antecedent + consequent)) # Result: ['I1', 'I3', 'I2']


antecedent_count = 0
for t in transactions:
    if all(item in t for item in antecedent):
        antecedent_count += 1

itemset_count = 0
for t in transactions:
    if all(item in t for item in full_itemset):
        itemset_count += 1

support = itemset_count / total_transactions

confidence = 0
if antecedent_count > 0:
    confidence = itemset_count / antecedent_count

print(f"--- Testing the Association Rule ---")
print(f"Rule: {antecedent} => {consequent}")
print(f"Full Itemset: {full_itemset}\n")
print(f"Total Transactions: {total_transactions}")
print(f"Count(antecedent): {antecedent_count} (Transactions containing {antecedent})")
print(f"Count(full itemset): {itemset_count} (Transactions containing {full_itemset})\n")

print(f"Support: {itemset_count} / {total_transactions} = {support:.2f} (or {support*100:.0f}%)")
print(f"Confidence: {itemset_count} / {antecedent_count} = {confidence:.2f} (or {confidence*100:.0f}%)")