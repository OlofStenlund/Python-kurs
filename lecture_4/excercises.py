class Course: # Create class
    def __init__(self, course_name: str, code: int, credits: int): # Define what arguments will be needed when calling the class
        self.course_name = course_name
        self.code = code
        self.credits = credits
        # __init__ is a constructor
    
    def __str__(self) -> str: # Function to return a string # Functions in classes are called FUNCTIONS
        return f"Kursen heter {self.course_name}, har kod {self.code} och ger {self.credits} poäng" # contents of the strin


kurs1 = Course("Python 1", "101", "25") # create object of class Course, input values
print(kurs1) # Print the results

class Teacher(Course):
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, age: int, course_name: str, code: int, credits: int):
        super().__init__(course_name, code, credits)
        self.first_name = first_name
        self.last_name = last_name
        self. email = email
        self.phone = phone
        self.age = age

    def __str__(self) -> str:
        return f"The course is called {self.course_name}, gives you {self.credits} points, and is held by {self.first_name} {self.last_name}, age {self.age}"

Lasse = Teacher("Lasse", "Karlsson", "lassemajja@python.com", "0125431", 43, "Python", 101, 25)
print(Lasse)

class Student(Course):
    def __init__(self, first_name: str, last_name: str, age: int, course_name: str, code: int, credits: int):
        super().__init__(course_name, code, credits)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f"{self.first_name} {self.last_name}"

stud1 = Student("Olof", "Stenlund", 33, "Python", 101, 25)
print(stud1.full_name)

