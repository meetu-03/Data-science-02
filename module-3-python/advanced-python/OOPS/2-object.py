'''
what is object?
1.object is instance of class
2.an object is an exmaples of class 
'''

class car:
    name="dodge"
    def __init__(self,carname,price):
        self.carname=carname
        self.price=price

obj=car("BMW",2200000)
print("car:",obj.name)
print("price:",obj.price)      
