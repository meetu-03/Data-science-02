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

