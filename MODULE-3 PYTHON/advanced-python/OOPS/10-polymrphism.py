# polymorfisum means same opration used by difrent behaviour that is calld polymrphism
# is is allows fuction aru method with same name to work as difrently behavior 
#typs of polymrphism    there are 2 type of that
# 1- method overloading
# 2- method overriding




class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())