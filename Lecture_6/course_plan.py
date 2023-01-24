from typing import List

class Students:

    def __init__(self, name: str):
        self.name = name

class Lesson:

    def __init__(self, title: str, description: str, time_in_hours: int):
        self.title = title
        self.description = description
        self.time_in_hours = time_in_hours

class Teacher:

    def __init__(self, name: str, company: str, skills: List[str]):
        self.name = name
        self.company = company
        self.skills = skills

class Course:
    def __init__(self, name: str, code: str, credits: int, teacher: Teacher, student: List[Students], lessons: List[Lesson]):
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher
        self.student = student
        self.lessons = lessons

    def __str__(self):
        student: str
        lessons: str
        for student in self.student:
            student += f"{student.name}"
        for lesson in self.lessons:
            lessons += f"{lesson.title}"
        string = f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits}"
        string += f"Lärare: {self.teacher.name}" # since self.teacher is a class, use self.teacher.name to access the name of the teacher
        string += f"Elever: {student}"
        string += f"Lektioner: {lessons}"
        return string 


def main():
    course = Course("Python 101", "DS_22_Python", 40, 
                Teacher("Anton", "Mujina", ["Python", "JavaScript", "Retrun"]), # Strings, not objects? # Creates an object of the Course-Class, and inside of it creates a Teacher object
                [Students("Sven"), Students("Anna"), Students("Liam"), Students("Rafad"), Students("Gina"), Students("David")],
                [Lesson("Repetition", "Vi repeterar allt vi gjort", 4),
                Lesson("Calsses", "Nothing works", 3)])
    print(course)


main()