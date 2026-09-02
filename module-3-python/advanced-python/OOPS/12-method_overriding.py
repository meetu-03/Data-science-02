#overriding is perfomed any opararions aor task using same fuction pass with diffrent argument that is calld method_overriding


class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())
