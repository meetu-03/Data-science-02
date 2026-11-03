#3.Write a function called format_price(price, currency='INR') that returns a string like '₹500' if currency is 'INR', or '$500' if currency is 'USD'.


def formate_price(price,currency="INR"):
    if currency =="INR":
        return "₹" + str(price)
    else:
        return "$" + str(price)

print(formate_price(480))
print(formate_price(480,"USD"))    
