#---------Static methods----------
# Cannot change the class


class Person:
    
    def __init__(self, name: str):
        self.name = name

    def printer(self):
        print("I am", self.name)

# Statci method, does not take self as argument, as it does not affect the class
# Must use decorator to make it static
    @staticmethod
    def say_hi():
        print("Hi")

olof = Person("olof")
# olof.say_hi()
# olof.printer()


# __init__ is only needed when we store data in a class. Since the class only contains static methods, nothing will be altered or stored
# Static methods are functions connected to a class
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtrace(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        return a / b

# We can now easily access the methods using class.method(arguments)
resadd = Calculator.add(1,2)
ressub = Calculator.subtrace(5,4)
# print(resadd, ressub)

## Try to import the calculator into another file and use it