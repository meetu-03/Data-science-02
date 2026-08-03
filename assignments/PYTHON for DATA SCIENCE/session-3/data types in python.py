# 1. Declare four variables in Python: your age as an int, your height in centimeters as a float, your name as a str, and whether you have a Spotify account as a bool. Print each variable and use the type() function to display its data type.

# ANSWER...

name = "Meetu"
age = 20
height = 170.5
has_spotify_account = True

print(name)
print(type(name))  #str
print(age)       
print(type(age))   #int
print(height)
print(type(height))     #float
print(has_spotify_account)
print(type(has_spotify_account))  #bool

# 2 .Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and returns the total as a float. Print the result for a sample Flipkart-style cart.<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>

# ANSWER... 

total_cart_amount = 0.0
prices = ['199.99', '49', '350.75']

for price in prices:
    total_cart_amount += float(price)

print("Total cart amount:", total_cart_amount)

 #599.64



 # 3.Create a script that asks the user to input their cricket score as a string, converts it to an int, and prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.<br><br><em><strong>Constraint:</strong> Use input(), int(), and if-else.</em>

# ANSWER...

score = input("Enter your cricket score: ")

score = int(score)

if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")



# 4..Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type.<br><br><em><strong>Hint:</strong> The bool() function alone won’t work as expected. Think about string comparison.</em> 

# ANSWER...

is_premium = 'True'
is_premium = is_premium == 'True'
print(is_premium)
print(type(is_premium))
