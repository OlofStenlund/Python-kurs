
# Setting up a basic superclass


from typing import List


class Course1:
    name: str
    code: str
    credits: int

    def __init__(self, name: str, code: str, credits: int):
        self.name = name
        self.code = code
        self.credits = credits

    def __str__(self):
        string = ""
        string += f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        return string

klass1_kurs1 = Course1("Python", "DC_22_Python", 40)
# print(klass1_kurs1) # Prints "", the empty string
# print(klass1_kurs1.name) # Prints the name of the course


#-----part 2----

class Teacher2:
    name: str
    age: int
    employer: str
    skills: List[str] # A list of strings, List being imported from typing

    def __init__(self, name: str, age: int, employer: str, skills: List[str]):
        self.name = name
        self.age = age
        self.employer = employer
        self.skills = skills

class Course2:
    name: str
    code: str
    credits: int
    teacher: Teacher2 # Must be defined before being used

    def __init__(self, name: str, code: str, credits: int, teacher: Teacher2): # Assign the class here
                # An object of another class is created in this class   
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher # teacher=teacher, self reference, not reference to class

    def __str__(self):
        string = ""
        string += f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Lärare: {self.teacher.name}"
        return string


course2_obj1 = Course2("Python", "DS_22_göteborg0", 40, 
            Teacher2("Anton", 30, "Mujna", ["Python", "mumbling"])) 
            # Teacher refers to the argument teacher: Teacher2, in the init-function of Course2
            #             
# print(course2_obj1.teacher.name) # In object course2_obj1, go to object teacher (of Teacher class), and look at name value
# print(course2_obj1) # Prints the __str__ of course2_obj1
# print(course2_obj1.teacher.skills[1]) # prints the second item in the skills-list in teacher in course2_obj1

#-------Part 3--------
# Add student class

# Teacher contains a list of string, students contain a list of objects.

class Teacher3:
    name: str
    age: int
    employer: str
    skills: List[str] 

    def __init__(self, name: str, age: int, employer: str, skills: List[str]):
        self.name = name
        self.age = age
        self.employer = employer
        self.skills = skills

class Students3:
    name: str
    def __init__(self, name):
        self.name = name

class Course3:
    name: str
    code: str
    credits: int
    teacher: Teacher3 
    students: List[Students3] # Many students, they will be a list

    def __init__(self, name: str, code: str, credits: int, teacher: Teacher3, student: List[Students3]): 
        # List of students, as we will define a few of them to add to the course
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher 
        self.students = student

    def __str__(self):
        stud = "" # Local variable that is an empty string. Must use "="
        for i in self.students: # Refers to the student-argument in __init__, not the local variable!!
            stud += f"{i.name}, " # Populates the string with student names
        # This is probably not needed, since we just converted a list to a string
        studlist = []
        for i in self.students: # Creates a list, how do we print the elements?
            studlist.append(i.name)
        string = ""
        string += f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Lärare: {self.teacher.name} \n"
        #string += f"Studenter {self.students}" # Returns infor about each element of the list
        string += f"Studenter: {stud}" # self. not needed, as we print the local variable created above
        # Fuigure out how to print the elements of studlist
        string += f"Studentlista: {studlist}" # Prints the list, not the elements
        return string

course3_obj1 = Course3("Python", "DS_22_göteborg", 40, 
            Teacher3("Anton", 30, "Mujna", ["Python", "mumbling"]),
            [Students3("Johan"), Students3("Oda"), Students3("Offelia"), Students3("Rojan")]) # List of students.in the list, each element must be defined as class students3


#print(course3_obj1)


#--------Part 4-------
# Add Lessons class
 
class Lessons4:
    title: str
    description: str
    time_in_hours: int

    def __init__(self, title: str, description:str, time_in_hours: int):
        self.title = title
        self.description = description
        self.time_in_hours = time_in_hours


class Teacher4:
    name: str
    age: int
    employer: str
    skills: List[str] 

    def __init__(self, name: str, age: int, employer: str, skills: List[str]):
        self.name = name
        self.age = age
        self.employer = employer
        self.skills = skills

class Students4:
    name: str
    def __init__(self, name):
        self.name = name

class Course4:
    name: str
    code: str
    credits: int
    teacher: Teacher4
    students: List[Students4] # Many students, they will be a list
    lessons: List[Lessons4]

    def __init__(self, name: str, code: str, credits: int, teacher: Teacher4, student: List[Students4], lessons: List[Lessons4]): 
        # List of lessons, just as with students
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher 
        self.students = student
        self.lessons = lessons

    def __str__(self):
        stud = "" # Local variable that is an empty string. Must use "="
        for i in self.students:
            stud += f"{i.name}, " 
        lessonlist = "" # Treat lessons just like students, add the elements to a str
        for i in self.lessons:
            lessonlist += f"{i.title}, "
        string = ""
        string += f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Lärare: {self.teacher.name} \n"
        string += f"Studenter: {stud}" # self. not needed, as we print the local variable created above
        string += f"Lektionnamn: {lessonlist}" # self. not needed, as we print the local variable created above
        return string

course4_obj1 = Course4("Python", "DS_22_göteborg", 40, 
            Teacher4("Anton", 30, "Mujna", ["Python", "mumbling"]),
            [Students4("Johan"), Students4("Oda"), Students4("Offelia"), Students4("Rojan")],
            [Lessons4("Intro", "job", 2), Lessons4("This is fun", "job", 2), Lessons4("...what?", "job", 2), Lessons4("Fuck my life", "job", 2), Lessons4("Welcome to McDonalds, can I take your order?", "job", 2)])

# print(course4_obj1)


#--------Step 5-------

# Change and update. 
# global functions and variables, loops to give choises and receive input

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
    teacher: Teacher4
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
        string += f"Studenter: {stud} \n" 
        string += f"Lektionnamn: {lessonlist}" 
        return string

    def update_teacher(self, teacher: Teacher5): # Create method to update teacher
        self.teacher = teacher # teacher refers to self.teacher in Course5?

    def add_student(self, student: Students5):
        self.students.append(student) # Apparently, this "is what we want to do"???

    def add_lesson(self, lesson: Lessons5):
        self.lessons.append(lesson) # lessons refers to self.lessons in Course5?

# global function, not tied to class
def print_choises(choices: List[str]): # Takes in variable "choises" defined in the while-loop in main()
    for i, choice in enumerate(choices): # Enumerate makes choises into keyvalue pair, assigns the number to i and str to choise
        # so you can loop by two variables, in this case i and choice
        print(f"{i} {choice}")

def run_choices(choice: int, course5: Course5 ):
    if choice == 0:
        exit()
    elif choice == 1:
        course5.update_teacher(Teacher5("Ushita", 32, "Gaddr", ["slow", "kind"]))
    elif choice == 2:
        course5.add_student(Students5("Bajshanna"))
    elif choice == 3:
        course5.add_lesson(Lessons5("fakkabout", "No thanks", 12))
    elif choice == 4:
        print(course5)

class CustomError(Exception): #What is exception, why do we take it as an argument?
    pass

def main():
    course5 = Course5("Python", "DS_22_göteborg", 40, 
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
            run_choices(userinput_int, course5)
        

main()