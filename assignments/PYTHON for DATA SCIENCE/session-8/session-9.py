#1.Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount rate to the given price.

def calculate_final_price(price,discount_rate):
    discount=price*discount/100
    final_price =price - discount
    return final_price


print(calculator_final_price(12000,20))
