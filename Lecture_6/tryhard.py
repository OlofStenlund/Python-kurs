
from typing import List


class Lessons5:
    title: str
    description: str
    time_in_hours: int

    def __init__(self, title: str, description:str, time_in_hours: int):
        self.title = title
        self.description = description
        self.time_in_hours = time_in_hours

class Teacher5:
    name: str
    age: int
    employer: str
    skills: List[str] 

    def __init__(self, name: str, age: int, employer: str, skills: List[str]):
        self.name = name
        self.age = age
        self.employer = employer
        self.skills = skills

class Students5:
    name: str
    def __init__(self, name):
        self.name = name

class Course5:
    name: str
    code: str
    credits: int
    teacher: Teacher5
    students: List[Students5] 
    lessons: List[Lessons5]

    def __init__(self, name: str, code: str, credits: int, teacher: Teacher5, student: List[Students5], lessons: List[Lessons5]): 
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher 
        self.students = student
        self.lessons = lessons

    def __str__(self):
        stud = "" 
        for i in self.students:
            stud += f"{i.name}, " 
        lessonlist = "" 
        for i in self.lessons:
            lessonlist += f"{i.title}, "
        string = ""
        string += f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Lärare: {self.teacher.name} \n"
        string += f"Studenter: {stud}" 
        string += f"Lektionnamn: {lessonlist}" 
        return string

    def update_teacher(self, teacher: Teacher5): # Create method to update teacher
        self.teacher = teacher

    def add_student(self, student: Students5):
        self.student.append(student) # Apparently, this "is what we want to do"???

    def add_lesson(self, lesson: Lessons5):
        self.lesson.append(lesson)

# global function, not tied to class
def print_choises(choices: List[str]): # Takes in variable "choises" defined in the while-loop in main()
    for i, choice in enumerate(choices): # Enumerate makes choises into keyvalue pair, assigns the number to i and str to choise
        # so you can loop by two variables, in this case i and choice
        print(f"{i} {choice}")

def run_choices(choice: int, course: Course5 ):
    if choice == 0:
        exit()
    elif choice == 1:
        course.update_teacher(Teacher5("Ushita", 32, "Gaddr", ["slow", "kind"]))
    elif choice == 2:
        course.add_student(Students5("Bajshanna"))
    elif choice == 3:
        course.add_lesson(Lessons5("fakkabout", "No thanks", 12))
    elif choice == 4:
        print(course5_obj1)

class CustomError(Exception): #What is exception, why do we take it as an argument?
    pass

def main():
    course5_obj1 = Course5("Python", "DS_22_göteborg", 40, 
                Teacher5("Anton", 30, "Mujna", ["Python", "mumbling"]),
                [Students5("Johan"), Students5("Oda"), Students5("Offelia"), Students5("Rojan")],
                [Lessons5("Intro", "job", 2), Lessons5("This is fun", "job", 2), Lessons5("...what?", "job", 2), Lessons5("Fuck my life", "job", 2), Lessons5("Welcome to McDonalds, can I take your order?", "job", 2)])

    choices = ["Exit", "Update teacher", "Add student", "Add lesson", "Print course"] # Create variable choises which is a list of strings
    while True:
        print_choises(choices)
        userinput = input("Choose an option: ")
        # Try exept to make sure the input is valid
        try:
            userinput_int = int(userinput.strip()) # If this returns false, we will skip to the first except(valueerror)
                                # Strip strips all the empty space
            if not 0 <= userinput_int < len(choices):
                raise CustomError
        except ValueError: # to catch value errors, ie, when number is wrong
            print("Not a valid number")
        except CustomError: # to catch out custom errorcheck "CustomError". Must be created as a class with "Exception" as an argument
            print("Invalid choice")
        else:
            run_choices(userinput_int, course5_obj1)
        

main()