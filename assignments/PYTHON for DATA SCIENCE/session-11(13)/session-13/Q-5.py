#Write a function called safe_divide_for_zomato that takes two numbers (bill amount and number of people), uses try, except, else, and finally to divide the bill and print the result, print a custom error if division by zero, and always print "Split calculation done" at the end.



def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        result = bill_amount / number_of_people
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Each person should pay:", result)
    finally:
        print("Split calculation done.")

safe_divide_for_zomato(1000, 4)
safe_divide_for_zomato(1000, 0)