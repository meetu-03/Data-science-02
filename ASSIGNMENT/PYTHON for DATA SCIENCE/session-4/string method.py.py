# 1.Take the string 'Flipkart-Sale2024' and use string methods to convert it to lowercase, replace the dash with a space, and print the result.

# ANSWER...

string = 'Flipkart-Sale2024'
string = string.lower()
string = string.replace('-', ' ')
print(string)



# 2.Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>

# ANSWER...

product_name = ' OnePlus Nord-CE 3 '
product_name = product_name.strip()
product_name = product_name.upper()
product_name = product_name.replace('-', ':')
print(product_name) 


# 3.Write a function split_product_code(product_code) that takes a string like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.


# ANSWER...

def split_product_code(product_code):
 return product_code.split('-')  



# 4.Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.


# ANSWER...

string = 'Spotify_Premium_Offer'
premium_word = string[8:15]  # Slicing to get 'Premium'
print(premium_word)


# 5.Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 'Deal: Myntra Shirt is available at ₹799.50 only!' using string formatting.

# ANSWER...

product = 'Myntra Shirt'
price = 799.5
print(f"Deal: {product} is available at ₹{price:.2f} only!")



