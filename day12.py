#Simple class
class car:
    pass

c = car()

#Class with attributes
class Person:
    name = "Cristi"
    age = 35

p = Person()
print(p.name)
print(p.age)

#Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

cristi = Person("Cristi", 35)
violeta = Person("Violeta", 29)

cristi.greet()
violeta.greet()

#Class with add and subtract methods
class AddSubtract:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

values = AddSubtract(10, 30)
print(values.add())
print(values.subtract())


