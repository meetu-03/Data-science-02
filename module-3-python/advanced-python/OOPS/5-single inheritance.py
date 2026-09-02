'''
what is single inheritnace?
 
- A one peret class access by its only one child class i.e. S I 
- A -> B

'''

# syntax


'''
class A:
    creat member function
    def __init__(self):
        body member fuction

def info():
    body if member fuction    
    

class B(A):
    member fuction():

    
    
'''



class A:
    def __init__(self,name):
        self.name=name

    def info(self):
        print("the name of use a :",self.name)
class B(A):
    def add(self,adress):
        self.adress=adress
        print("the adress of user is:",self.adress)            


obj=B("meet")
obj.info()
obj.add("morbi")



class A:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("The name of user is:", self.name)


class B(A):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def address_info(self):
        print("The address of user is:", self.address)


obj = B("Meet", "Morbi")

obj.info()
obj.address_info()