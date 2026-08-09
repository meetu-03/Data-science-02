'''
# Task 1: Student Grade Calculator
Write a Python program to input student marks and display the grade:
- 90 and above: Grade A
- 75 to 89: Grade B
- 50 to 74: Grade C
- 35 to 49: Grade D
- Below 35: Fail
'''

marks=int(input("enter your marks:"))
if marks>=90:
	print("your grade is A")
elif marks>=75:
	print("your grade is B")
elif marks>=50:
	print("your grade is C")
elif marks>=35:
	print ("your grade is D")
else:
	print("you are failed")

'''
# Task 2: Electricity Bill Calculator
Write a Python program to calculate electricity charges based on units consumed:
- First 100 units: ₹5/unit
- Next 100 units: ₹7/unit
- Above 200 units: ₹10/unit

'''

bill=int(input("enter your used units"))
if bill<=100:
	print("your payable bill is:",bill*5)
elif bill<=200:
	print("your payable bill is:",(100*5)+(bill-100)*7)
else:
	print("your payable bill is:",(100*5)+(100*7)+(bill-200)*10)


'''
## Task 3: Age Category Checker
Write a Python program to check a person's category based on age:
- Below 13: Child
- 13 to 19: Teenager
- 20 to 59: Adult
- 60 and above: Senior Citizen

'''

age=int(input("enter your age"))
if age<=13:
	print("you are child")
elif age<=19:
	print("you are teenager")
elif age<=59:
	print("you are adult")
else:
	print("you are senior citizen")



'''
## Task 4: Number Checker
Write a Python program to check whether a number is:
- Positive
- Negative
- Zero

'''

number=int(input("enter number:"))
if number >0:
	print("positive")
elif number<0:
	print("negative")
else:
	print("0")	


'''
## Task 5: Even or Odd Number
Write a Python program to check whether the entered number is even or odd.

'''

number=int(input("enter number:"))
if number%2==0:
	print("even")
else:
	print("odd")



'''
## Task 6: Largest Among Three Numbers
Write a Python program to input three numbers and find the largest number using conditional statements.

'''

number=int(input("enter number"))
number1=int(input("enter number"))
number2=int(input("enter number"))
if number>number1:
	print("number is larg")
elif number1>number2:
	print("number1 is larg")
else:
	print("number2 is larg")



'''
## Task 7: Driving License Eligibility
Write a Python program to check driving license eligibility:
- Age 18 or above: Eligible
- Below 18: Not Eligible

'''


age=int(input("enter your age"))
if age>=18:
	print("you are eligible")
else:
	print("you are not eligible")



'''
## Task 8: Temperature Checker
Write a Python program to display weather conditions:
- Below 10°C: Cold
- 10°C to 30°C: Normal
- Above 30°C: Hot

'''

temp=int(input("enter temp"))
if temp<=10:
	print("cold")
elif temp<=30:
	print("normal")
else:
	print("hot")	


'''
## Task 9: Login Authentication System
Write a Python program to check username and password:
- Correct username and password: Login Successful
- Wrong details: Invalid Login

'''

user = "meetu"
password = "meetuuu@03"

user=str(input("enter your user name"))
password=str(input("enter your password"))
if user=="meetu" and password=="meetuuu@03":
	print("logine aproved")
else:
	print("user or pass wrong")

	
'''
## Task 10: Simple Calculator
Write a Python program to perform operations based on user choice:
- Addition
- Subtraction
- Multiplication
- Division
'''	
	
print("######Calculator######")
print("Enter your choice:")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
while True:
    choice = int(input("Enter your choice:"))
    if choice==1:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Addition is:",a+b)
    elif choice==2:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Subtraction is:",a-b)
    elif choice==3:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Multiplication is:",a*b)
    elif choice==4:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print("Division is:",a/b)
    else:
        print("Invalid choice")
    

'''
## Task 11: Employee Bonus Calculator
Write a Python program to calculate employee bonus:

- Salary above ₹50000: 20% bonus
- Salary between ₹30000 and ₹50000: 10% bonus
- Below ₹30000: 5% bonus
'''


salary=int(input("enter your salary"))
if salary>=50000:
	print("your bonus is :",salary*0.2)
elif salary>=30000:
	print("your bonus is :",salary*0.1)	
else:
	print("your bonus is :",salary*0.05)

'''
## Task 12: Movie Ticket Price Calculator
Write a Python program to calculate ticket price:
- Age below 12: ₹100
- Age 12 to 60: ₹200
- Age above 60: ₹150
'''


age=int(input("enter your age"))

if age<=12:
	print("your payable price is :",100)
elif age<=60:
	print("your payabelprice is :",200)
else:
	print("your payable price is :",150)


'''
## Task 13: Bank Withdrawal System
Write a Python program to check withdrawal:
- Balance sufficient: Allow withdrawal
- Insufficient balance: Show error message

'''

balance=10000
withdrawal=int(inptut("enter your W amount"))
if balance>withdrawal:
	print("you are eligeble for withdrawal")
else:
	print("you are not eligable for withdrawal")

'''
## Task 14: Shopping Discount Calculator
Write a Python program to apply discount:
- Purchase above ₹10000: 20% discount
- Purchase above ₹5000: 10% discount
- Otherwise: No discount
'''	


amount=int(input("enter your ammount"))
if amount>=10000:
	print("your discount is :",amount*0.2)
elif amount>=5000:
	print("your discount is :",amount*0.1)
else:
	print("you have no discount please buy more")		



'''
## Task 15: Traffic Signal System
Write a Python program to display action based on traffic light color:
- Red: Stop
- Yellow: Wait
- Green: Go

'''

signal=str(input("enter signal"))
if signal=="red":
	print("stop")
elif signal=="yellow":
	print("wait")
elif signal=="green":
 print("go")
else:
	print("invaid signal")		

'''
## Task 16: Voter Eligibility Checker
Write a Python program to check voting eligibility:
- Age 18 or above: Eligible to vote
- Below 18: Not eligible to vote
'''	

age=int(input("enter your age"))
if age>=18:
	print("you are eligeble")
else:
	print("you are not eligeble")

'''
## Task 17: Password Strength Checker
Write a Python program to check password strength:
- Length less than 6: Weak
- Length 6 to 10: Medium
- Length above 10: Strong
'''

password=str(input("enter your password"))
if len(password)<=6:
	print("pass is weak")
elif len(password)<=10:
	print("pass is medium")
else:
	print("pass i strong")	

	
		
'''
## Task 18: BMI Category Calculator
Write a Python program to calculate BMI category:
- BMI below 18.5: Underweight
- 18.5 to 24.9: Normal
- 25 to 29.9: Overweight
- 30 and above: Obese

'''

bmi=flote(input("enter your bmi"))
if bmi<18.5:
	print("under weight")
elif bmi<=24.9:
	print("normal")
elif bmi<=29.9:
	print("overweight")
else:
	print("obese")


'''
## Task 19: Mobile Data Plan Selector
Write a Python program to suggest a mobile plan:
- Data usage below 2GB: Basic Plan
- 2GB to 5GB: Standard Plan
- Above 5GB: Premium Plan

'''

d_used=int(input("enter your data used in gigabyte"))
if d_used<=2:
	print("basic plane")
elif d_used<=5:
	print("standerd plan")
else:
	print("premium plan")


'''
## Task 20: Exam Result Checker
Write a Python program to display result:
- All subjects marks >= 35: Pass
- Any subject below 35: Fail
- Marks above 90 in all subjects: Excellent Performance
'''

marks=int(input("enter all sub  marks"))
if marks>=90:
	print("you are genius")
elif marks>=35:
	print("you are pass")
else:
	print("you are fail")	