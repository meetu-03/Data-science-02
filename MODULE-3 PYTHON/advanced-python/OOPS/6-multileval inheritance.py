#what is multileval inheritance?

# A one perent class acces by its child class and its again and again ..


# syntax

class Grandfather:
    def house(self):
        print("Grandfather has a house")

class Father(Grandfather):
    def car(self):
        print("Father has a car")

class Son(Father):
    def bike(self):
        print("Son has a bike")

s = Son()
s.house()
s.car()
s.bike()

