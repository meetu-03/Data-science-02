# abstract class is hide some internal data from some users. 
# abstract is used for hiding data .
# when we create a class as abstract whenever create  its object.
# we access abstract class by another class.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog()
print(dog.make_sound())



