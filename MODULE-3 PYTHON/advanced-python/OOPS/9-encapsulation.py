#encapsulation is used to wrap up in single object i.e.called.....en..
#data acces in encapsulatiin by access modifier or privet,public,protected..
#encapsulation is used for visiblity of data via privet,public,protected


# public -- accessible anywhere i.e. public


class employee:
    def __init__(self,name):
        self.name=name # accessible via public
    # create a public method

    def display_employee(self):
        print(self.name)

obj=employee("meetu")
obj.display_employee   #accessible via public
print(obj.name)        #accessible anywhere




# privet : that can be accessible only inside pf class


class employee:
    def __init__(self,name):
        self.name=name

    def show_age(self,age):
        print(age)
    # privet mwthod 
    #
    def show_add(self):
        print("add is :",self.add)

    # crete an object            
        
obj=employee("meetu")
print(obj.name)    # accissible name
obj.show_age(20)   # accessible
obj.show_add()    # not accessible bcause it is privet 



# protectd : when method is protected ot should accessible only by one chid class


class employee:
    def __init__(self,name,age):
        self,name=name
        self.age=age

# call protected method
#
class subemployee(employee):
    def show_age(self):
        print("employee name is:",self.name,"employee age is:",self.age)         
        


obj=subemployee("meet",20)
obj.show.age # accessible becaus this is protected

