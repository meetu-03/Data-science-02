# task 3 Build a Python program that applies a tiered commission structure to delivery order data using
# functions, higher-order functions, and formatted console output.
'''
-Define a named function calculate_commission(amount) that returns 10% for amounts up to Rs 200, 15% for Rs 201–Rs 500, and 20% for amounts above Rs 500 using an if-elif-else block — do not use a lookup table or dictionary for this
'''

# ANSWER...

def calculate_commission(amount):
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    else:
        return amount * 0.20

'''
- Create a list of at least 8 order amounts that span all three tiers, then apply
calculate_commission across the list using map() with a lambda — store the result in a
variable called commissions; do not use a second for loop for this step.

'''

# ANSWER...

orders = [100, 200, 250, 350, 500, 600, 800, 1000]

commissions = list(map(lambda amount: calculate_commission(amount), orders))

print(commissions)


'''
Use filter() with a lambda to extract only the order amounts where the corresponding
commission exceeds Rs 60, storing the result in a list called high_value_orders.
'''

# ANSWER...

high_value_orders = list(
    filter(lambda x: x[1] > 60, zip(orders, commissions))
)

print(high_value_orders)


'''
Print three clearly labelled blocks: (1) a table showing each order amount and its calculated
commission rounded to 2 decimal places, (2) the total payout using sum() on the
commissions list, and (3) the high_value_orders list with a count of how many entries it
contains.

'''

# ANSWER...

# 1. Order Amount and Commission
print("\n--- Order Amount and Commission ---")

for amount, commission in zip(orders, commissions):
    print(f"Order Amount: Rs {amount} | Commission: Rs {commission:.2f}")


# 2. Total Payout
print("\n--- Total Payout ---")

total_payout = sum(commissions)
print(f"Total Payout: Rs {total_payout:.2f}")


# 3. High Value Orders
print("\n--- High Value Orders ---")

print("High Value Orders:", high_value_orders)
print("Count:", len(high_value_orders))


