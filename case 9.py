#  c - 55 Transaction Audit using Tuples
transaction = ("TXN101", 1500.0, "DEPOSIT")

txn_id, amount, txn_type = transaction
if amount < 0:
    print("Warning: Negative amount detected in", txn_id)
else:
    print(f"Valid {txn_type} of Rs.{amount} recorded for {txn_id}.")