"""
# example of operator 

1. Arithmetic operator
-. +,-,*,/,%,//,**

A=10
B=20
C=A+B
D=A-B
E=A*B
F=A/B

print(C)
print(D)
print(E)
print(F)


2. comparision operator
-. ==,!=,>,<,>=,<= 

a=10
b=12

print(a==b)
false (beacause both value are difrent and == used to indicate same value)

print(a!=b)
true (beacause != used to indicate difrent value)

print(a<b)
true (beacuase < is used to indicate higher value then first variable)

print(a>b)
false (beacause >used to indicate lower value then first variable )

print(a<=b)
true (beacause <= used to indicate value that it is same aur higher then first value )

print(a>=b)
false (beacause >= used to indicate value that it is same aur lower then first value)

3. logical operator
-. and, or, not 

a=10
b=20

print(a>b and b>12)
false (beacause and operator used to indicate both condition are true but here first condition is false)

print(a<b and b>12)
false (beacause and operator used to indicate both condition are true but here first condition is true but second condition is false)

print(a<b or b>12)
true (beacause or operator used to indicate either of the condition is true)

print(a>b or a<12)
true (beacause or operator used to indicate either of the condition is true)

print(a>b or b>22)
false (beacause or operator used to indicate either of the condition is true but here both condition are false)


### note: not opratore always shoes the opposite of the condition

print(not(a>b))
true (beacause not operator used to indicate the opposite of the condition)

print(not(a<b))
false (beacause not operator used to indicate the opposite of the condition)

4. assignment operator
-. =, +=, -=, *=, /=, %=, //=, **=  


a=10
a+=5
a-=5
a*=5
a/=5
a%=5
a//=5
a**=5   



print(a)
15 (beacause += operator used to indicate the addition of the value of variable with the value that is assigned to it)

print(a)
5 (beacause -= operator used to indicate the substraction of the value of variable with the value that is assigned to it)

print(a)
50 (beacause *= operator used to indicate the multiplication of the value of variable with the value that is assigned to it)

print(a)
2 (beacause /= operator used to indicate the division of the value of variable with the value that is assigned to it)

print(a)  (NOTE: in python % mean remainder means what vaule can be divided by the other value and what is the remainder(pachal vadheli rakam) of that value.)
0 (beacause %= operator used to indicate the modulus of the value of variable with the value that is assigned to it)

print(a)  (NOTE: in python // mean flor division but it can remove all decimal number after the main value)
2 (beacause //= operator used to indicate the floor division of the value of variable with the value that is assigned to it)

print(a) (NOTE: **1,2,3,4,5, mean squar,cube aur ghat)
100000 (beacause **= operator used to indicate the exponential of the value of variable with the value that is assigned to it)

5. bitwise operator
-. &, |, ^, ~, <<, >>     

a=10
b=12    

print(a>>b)
basically >> operator used to indicate the right shift of the value of variable with the value that is assigned to it)

(NOTE: bitwis oprerator mostly nt use in datat science so skip)


6. identity operator
-. is, is not   

a=[10,20]
b=a
a=[10,20]
b=[10,20]

print(a is b) (NOTE: identety operator is used to defina both variable are sae or not that under stored value )
true (beacause is operator used to indicate the both variable are same and point to the same object in memory)

print(a is not b)  (a=10,20 but b =a so both variable have same but is not so its wrong )
false (beacause is not operator used to indicate the both variable are not same and point to the same object in memory)

(both have sam value but bot hvae difrent file )

print(a is b)
false (beacause is operator used to indicate the both variable are same and point to the same object in memory but here both variable are not same so its wrong)

print(a is not b)
true (beacause is not operator used to indicate the both variable are not same and point to the same object in memory)


7. membership operator
-. in, not in       


number=[10,20,30,40,50]

print(10 in number)
true (beacause in operator used to indicate the value is present in the list or not)

print(60 in number)
false (beacause in operator used to indicate the value is present in the list or not)

(check list if value is present or not using membership operator)

8. increment operator
-. +=   

a=10
a +=1

print(a) (10+1=11 so it will print 11)
11 (beacause += operator used to indicate the addition of the value of variable with the value that is assigned to it)

9. decrement operator
-. -=

a=10
a -=5


print(a) (10-5=5 so it will print 5)
5 (beacause -= operator used to indicate the substraction of the value of variable with the value that is assigned to it)

10. exponential operator
-. **   


a=5
b=2


print(a**b)  (NOTE: ** used to find power)
25 (beacause ** operator used to indicate the exponential of the value of variable with the value that is assigned to it)


11. string concatenation operator
-. +

name="meetu"
sarname="patel"

print(name+sarname)
meetupatel (beacause + operator used to indicate the concatenation of the value of variable with the value that is assigned to it)

print(name+" "+sarname)
meetu patel  (if you need space so add" ")
"""
name = "Meetu"
sarname = "Patel"
"""
print(name + "\n" + sarname)
meetu
patel  (if you need new line so add "\n")   

"""


"""
a=10
b=12

print(a==b)
print(a!=b)
print(a<b)
print(a<=b)

print(a>b and b>12)
print(a<b and b>12)
print(a<b or b>12)
print(a>b or a<12)
print(a>b or b<22)
print(a>b or b>22)

print(not(a<b))
"""

number=[10,20,30,40,50]

print(60 in number)




a=10
a -=5

print(a)



a=5
b=2


print(a**b)

name="meetu"
sarname="patel"

print(name+sarname)
print(name+" "+sarname)

