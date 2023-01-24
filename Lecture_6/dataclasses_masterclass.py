

from typing import List


class LessonClass:
    title: str
    description: str
    hours: int
    def __init__(self, title: str, description: str, hours: int):
        self.title = title
        self.description = description
        self.hours = hours

class TeacherClass:
    name: str
    age: int
    employer: str
    skills: List[str]
        
    def __init__(self, name: str, age: int, employer: str, skills: List[str]):
        self.name = name
        self.age = age
        self.employer = employer
        self.skills = skills

class StudentClass:
    name: str

    def __init__(self, name:str):
        self.name = name

class CourseClass:
    name: str
    code: str
    credits: int
    course_teacher: TeacherClass
    course_students: List[StudentClass]
    course_lessons: List[LessonClass]

    def __init__(self, name: str, code: str, credits: int, course_teacher: TeacherClass, 
                    course_students: List[StudentClass], course_lessons: List[LessonClass]):
        self.name = name
        self.code = code
        self.credits = credits
        self.course_teacher = course_teacher
        self.course_students = course_students
        self.course_lessons = course_lessons

    def __str__(self):
        student_list = ""
        for i in self.course_students:
            student_list += f"{i.name}, "
        lesson_list = ""
        for i in self.course_lessons:
            lesson_list += f"{i.title}, "
        full_string = ""
        full_string += f"Kurs: {self.name} \n Kod: {self.code} \n Poäng: {self.credits} \n"
        full_string += f"Lärare: {self.course_teacher.name} \n Sudenter: {student_list} \n Lektionnamn: {lesson_list}"
        return full_string

example1 = CourseClass("Python", "DS_2022", 40, 
            TeacherClass("Anton", 30, "Mujina", ["Python", "Teaching"]),
            [StudentClass("Olof"), StudentClass("Ilja"), StudentClass("Anna"), StudentClass("Pjotr")],
            [LessonClass("intro", "What is python?", 3), LessonClass("Confusion time", "Time to get messy", 3), LessonClass("What!?", "Let's go bowling", 2)])

print(example1)