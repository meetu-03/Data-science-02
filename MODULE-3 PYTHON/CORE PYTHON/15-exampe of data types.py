"""
1. string: A sequence of characters, used to represent text.
-  '' and "" are used to define string values in Python.
-  any number,text,emoji can be used in string values.

name="meetu"
  print(name) # Output: meetu

2. integer: A whole number, positive or negative, without decimals.
-  int() function is used to convert a value to an integer data type.
-  int savade all numbers without decimal point.


age=20
print(age)


3. float: A number that has a decimal point.
-  float() function is used to convert a value to a float data type.   


waight=10.5
print(waight)


4. boolean: A data type that can have one of two values: True or False.
-  bool() function is used to convert a value to a boolean data type.   


a=10
b=15

print(a>b)   #true
print(a<b)   #false


5. list: A collection of items that can be of different data types, enclosed in square brackets [].
-  list() function is used to convert a value to a list data type.  
- list is mutable data type in python.
- we can change the value of list after it is created.
- we can change any list at runtime of execution.
- we can store dupilicate value in list.
- list is ordered data type in python.
- list does not store value in 01,02,03,04,05,06,07,08,09,10 format in python.


employee=["brijesh","meetu","sandeep"]
print(employee)

employee.append("hetvi")
print(employee)

6. tuple: A collection of items that can be of different data types, enclosed in parentheses ().
-  tuple() function is used to convert a value to a tuple data type.    
- tuple is immutable data type in python.
- we can not change the value of tuple after it is created.
- we can not change any tuple at runtime of execution.
- we can store dupilicate value in tuple. 
- tuple is ordered data type in python.
- 

t=("meetu",13,03,2006)
print(t)

7.set: A collection of unique items that can be of different data types, enclosed in curly braces {}.q
- set() function is used to convert a value to a set data type.
- set is mutable data type in python.
- we can change the value of set after it is created.
- we can change any set at runtime of execution.
- we can not store dupilicate value in set.
- set is unordered data type in python.
- we can add,delet,update value in set at runtime of execution.


s={"meetu",13,03,2006}
print(s)

8. dictionary: A collection of key-value pairs, enclosed in curly braces {}.
- dictionary() function is used to convert a value to a dictionary data type.
- dictionary is mutable data type in python.
- we can change the value of dictionary after it is created.
- we can change any dictionary at runtime of execution.
- we can not store dupilicate key in dictionary.
- dictionary is unordered data type in python.


D={"name":"meetu","age":20,"waight":10.5}
print(D)   

D["city"]="morbi"
D["country"]="india"

D["name"]="brijesh"
print(D)

del D["age"]

9. None: A special data type that represents the absence of a value or a null value.
- None is often used to indicate that a variable has no value or that a function does not return anything.

a=none
print(a)


"""

# RUN

#string

name="meetu"
print(name)

print(type(name))

#int

age=20
print(age)
print(type(age))
    
#float

waight=10.5
print(waight)
print(type(waight))

#boolean    

a=10
b=15

print(a>b)
print(a<b)
print(type(a>b))
print(type(a<b))

#list

employee=["brijesh","meetu","sandeep","meetu"]
print(employee)

employee.append("hetvi")
print(employee)
print(type(employee))

#tuple

t=("meetu",13,3,2006)
print(t)
print(type(t))


# set
s={"meetu",13,3,2006}
print(s)
print(type(s))
s.add("hetvi")

# dictionary

D={"name":"meetu","age":20,"waight":10.5}
print(D)   
D["city"]="morbi"
D["country"]="india"
print(D)
D["name"]="brijesh"
print(D)
del D["name"]
print(D)

print(type(D))