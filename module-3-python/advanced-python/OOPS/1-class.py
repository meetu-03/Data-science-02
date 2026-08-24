"""
# what is class?
- a class is noting whenever we can not creat its objact
- a class is group of its member and member fuction
- a class is blue or shadow of print of any object

"""


# syntax of class
'''
class className:
    body of class
        creat a fuction:
        body of mmber function
'''
# creat an object of class


class A:
    #define an atributes of class
    name="meetu"
    # creat a constuctor
    def __init__(self,age,name):
        self.age=age  #instance of class
        self.name=name 

# creat an object of class A
obj = A(20,"meet")  #A is an object of class A
print(obj.age)
print(obj.name)





         