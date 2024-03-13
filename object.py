'''Dependence between objects is what is called object relaionship.- how objects interact and relate to each other.
 - representation is done using classes and instances.


 One to many
 -idea: school system of students and courses ; one student can have many courses'''

class Student :
    def __init__(self, name) -> None:
        self.name = name
        self.courses=[]


    def enroll(self, course) :
        self.courses.append(course)
        course.students.append(self)

class Course :
    def __init__(self, name) :
        self.name = name
        self.students = []
    
    def add_student(self,student) :
        self.students.append(student)
        student.courses.append(self)


 
