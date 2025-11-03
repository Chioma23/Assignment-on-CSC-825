from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Person(ABC):
    def __init__(self, name):   # fixed __init__
        self._name = name       
    @abstractmethod
    def role(self):
        pass
# ---------- Inheritance & Encapsulation ----------
class Student(Person):
    def __init__(self, name):   # fixed __init__
        super().__init__(name)
        self._courses = {}
    def role(self):
        return "Student"
    def enroll(self, course):
        self._courses[course] = None
        print(f"{self._name} enrolled in {course}")
    def set_grade(self, course, grade):
        if course in self._courses:
            self._courses[course] = grade
        else:
            print(f"{self._name} is not enrolled in {course}.")
    def view_grades(self):
        print(f"\nGrades for {self._name}:")
        if not self._courses:
            print(" - No courses enrolled yet.")
        for c, g in self._courses.items():
            print(f" - {c}: {g if g else 'Not graded yet'}")
class Teacher(Person):
    def __init__(self, name):   # fixed __init__
        super().__init__(name)
    def role(self):
        return "Teacher"
    def assign_grade(self, student, course, grade):
        if isinstance(student, Student):
            student.set_grade(course, grade)
            print(f"{self._name} gave {student._name} a '{grade}' in {course}")
        else:
            print("Error: Only a student can receive grades.")
# ---------- Polymorphism ----------
def describe(person):
    print(f"{person._name} is a {person.role()}.")
# ---------- Demonstration ----------
teacher = Teacher("Mr. Smith")
student = Student("Chioma")
describe(teacher)
describe(student)
student.enroll("Mathematics")
teacher.assign_grade(student, "Mathematics", "A")
student.view_grades()
