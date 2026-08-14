"""
# what is data type in variable in python?

-data type is a classification that specifies which type of value a variable has and what type of mathematical,
-relational or logical operations can be applied to it without causing an error. In python, data type is used to
-define the type of variable.
-data type in simple words is a type of value that is assigned to a variable in python. In python,
-data type is used to define the type of variable.

# datatype list

- integer   (number)
- string    ("",''under all data are str)
- float      (decimal number like 10.23456152)
- undefined   
- null
- boolean
- tuple
- dictionary 
- list 
- set 

  

a=10          # int            ( " ",' ' is uesd for string value )
b=10.654545   #float           
c="brijesh"   #string
d='15455'     #string










"""


a="meetu"

print(type(a))

bill=int(input("enter your used units"))
if bill<=100:
	print("your payable bill is:",bill*5)
elif bill<=200:
	print("your payable bill is:",(100*5)+(bill-100)*7)
else:
	print("your payable bill is:",(100*5)+(100*7)+(bill-200)*10)
