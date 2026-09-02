#Build a Flipkart-style price-per-item calculator: take total cart amount and item count as input, perform division, and use try-except to catch and display a user-friendly message if the item count is zero.

def price_per_item(total_amount, item_count):
    try:
        print(total_amount / item_count)
    except ZeroDivisionError:
        print("Item count cannot be zero.")

price_per_item(1000, 5)
price_per_item(1000, 0)