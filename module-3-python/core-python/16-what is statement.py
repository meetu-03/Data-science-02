'''
# Python Statements

A **statement** is an instruction given to Python to perform an action.

## Types of Statements in Python

### 1. Single-Line Statement

A statement written in a single line.
'''

# python
x = 10
print(x)


'''
# 2. Conditional Statements in Python

A **conditional statement** is used to make decisions in Python based on a condition.

## Types of Conditional Statements

1. `if` statement
2. `if-else` statement
3. `if-elif-else` statement
4. Nested `if` statement

---

## 1. `if` Statement

Executes the code only when the condition is `True`.
'''
# python
age = 20

if age >= 18:
    print("Adult")



'''
# 3. Looping / Iterative Statements in Python

A **looping statement** is used to **repeat a block of code** multiple times.

## Types of Looping Statements

1. `for` loop
2. `while` loop

---

## 1. `for` Loop

The `for` loop is used to iterate over a sequence or range of values.
'''
### Example

## python
for i in range(5):
    print(i)


while True:

    choice = int(input("Enter Login with As: "))

    if choice == 1:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == 'customer@gmail.com' and password == 'customer@123':
            print("You are Logged in as customer successfully")
        else:
            print("Your credentials are invalid")

    elif choice == 2:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == 'admin@gmail.com' and password == 'admin@123':
            print("You are Logged in as Admin successfully")
        else:
            print("Your credentials are invalid")

    elif choice == 3:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == 'manager@gmail.com' and password == 'manager@123':
            print("You are Logged in as Manager successfully")
        else:
            print("Your credentials are invalid")

    elif choice == 4:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == 'employee@gmail.com' and password == 'employee@123':
            print("You are Logged in as Employee successfully")
        else:
            print("Your credentials are invalid")

    elif choice == 5:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == 'counceler@gmail.com' and password == 'counceler@123':
            print("You are Logged in as Counceler successfully")
        else:
            print("Your credentials are invalid")

    else:
        print("Selected wrong choice")