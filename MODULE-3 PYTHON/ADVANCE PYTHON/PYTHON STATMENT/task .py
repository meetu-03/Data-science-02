# # # print a start tangle pattrn write progrm to print 1 to 10 and find only even number between 1 to 10
# # # write a program to print multiplications of table 
# # # write a program to print find some of number from 1 to 100
# # # write a program to revers a str
# # # write a program to find some of list of elments
# # #  find largest number in a list
# # # print a numbe from 10 to 1 using while loop
# # # write a program of some of digits using whil loop
# # # write a program to count digit take input from users
# # # wirte a program to print star reves pattrns
# # # write a program to print sqaure patterns
# # # write a program to authentication pf [asssword if user input coorect pass word its authenticated login succesfull ptherwisw authicated in corect password if users countinue enter 3 attemps password fails you acc will be block
# # #



# #  print a start tangle pattrn write progrm to print 1 to 10 and find only even number between 1 to 10


for i in range(1,11):
    for star in range(i):
        print("*",end=" ")
    print( )    


# ## write a program to print square patterns

for i in range(1,11):
    for square in range(1,11):
        print("*",end=" ")
    print("\n")    

# ## print a number from 10 to 1 using while loop


num=int(input("enter number"))
for i in range(1,11):
    print(num,"x",i,"=",i*num)

#write a program to revers a str

str=str(input("enter str"))

rev=" "
for asd in str:
    rev=asd+rev
print(rev)    


# # # write a program to find some of list of elments

num=[1,25,35,15,45,55]
total=0
for abc in num:
    total+=abc
print(total)    

# #write a program to authentication of passsword if user input coorect pass word its authenticated login succesfull ptherwisw authicated in corect password if users countinue enter 3 attemps password fails you acc will be block

email="meetu@gmail.com"
password="meetu@03"

for attemp in range(1,4):
    email=input("enter email:")
    password=input("enter password:")

    if email=="meetu@gmail.com" and "password==meetu@03":
        print("you are login succesfully")
        break
    else:
        print("somethng went wrong")
else:
    print("you can't login at this time you have no more attempt to login")

# #write progrm to print 1 to 10 and find only even number between 1 to 10


for i in range(1,11):
    print(i)


for i in range(1,11):
   if i % 2 == 0:     # % use for remainder 
      print(i)
      


# #write a program to print find sum of number from 1 to 100
add=0
for i in range(1,101):
    add=add+i
print("total of 1 to 100 : ",add)

# ## # write a program to revers a str

str="meetu"
rev=" "

for i in str:
    rev= i+rev
print(rev)

# ## # write a program to find sum of list of elments

numbers = [12, 54, 54, 612, 65, 65, 34, 53]
summ = 0

for i in numbers:
    summ = summ + i

print(summ)

# #print a numbe from 10 to 1 using while loop

i=0
while i <10:
    i+=1
    print(i)



# #    write a program of sum of digits using whil loop


num = 52656
summ = 0

while num > 0:
    digit = num % 10         # % use as remainder
    summ = summ + digit
    num = num // 10           #// is remove last digit of nums

print(summ)


# # write a program to count digit take input from users


digit=13032006
count=0
while digit >0:
    count=count+1
    digit // 10
    print(count) 


    # count the digit


digit=input("number")
count=0

while digit>0:
    count=count+1
    digit // 10
print(count)

# write a program to count even and odd numbers
# find smallest number in any given list


#find smallest


number=[10,12,35,34,38,26]
smallest=number[0]

for i in number:
    if i<smallest:
        smallest=i
print(smallest)    


# #. Print numbers 1 to 10
# - Use `while`
# - Don't use `for`

i=0
while i <=10:
    print(i)
    i+=1

# #2. Print numbers 10 to 1
# - Use `while`

i=10
while i >=0:
    print(i)
    i-=1


#### 3. Print all even numbers from 2 to 20


for i in range(1,21):
     if i % 2==0:
         print(i)

## 4. Print all odd numbers from 1 to 19


for i in range(0,20):
    if i % 2!=0:
        print(i)

