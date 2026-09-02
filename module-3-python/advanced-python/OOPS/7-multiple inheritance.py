# multiple inheritance 

# A multiple inherutance used for 2 perent class properties acces with single child class

class Father:
    def car(self):
        print("Father has a car")

class Mother:
    def house(self):
        print("Mother has a house")

class Child(Father, Mother):
    def bike(self):
        print("Child has a bike")

c = Child()
c.car()
c.house()
c.bike()