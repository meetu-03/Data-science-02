#Create a generator function called order_id_generator that yields a new order ID (starting from 1001) each time it's called, similar to how Zomato or Swiggy generates unique order numbers.<br><br><em><strong>Hint:</strong> Use the yield statement inside a loop to generate the next ID.</em>

def order_id_generator():
    order_id = 1001

    while True:
        yield order_id
        order_id += 1


orders = order_id_generator()

print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))