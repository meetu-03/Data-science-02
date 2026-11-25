'''

- a consructor is a same name of class
- a consructor is same name of class whenever we creat an object of class consructor

'''

#constructor is in built fuction that can be definr as __init__(self) argument


class college:
    collegeName="omvvim"
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress

obj=college("DU","rajkot")
print(obj.name)
print(obj.adress)       


    
        