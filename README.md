**Name: Chioma Sarah Obinwanne**

**Course Code: 825**

**PG Number: PG202442998812**

**Overview**

This Python program demonstrates the four fundamental principles of Object-Oriented Programming (OOP) Abstraction, Encapsulation, Inheritance, and Polymorphism using a simple educational system with Person, Student, and Teacher classes.

**Code Description****

1️⃣ Abstraction

Implemented through the abstract base class Person.

The @abstractmethod decorator ensures that every subclass (Student, Teacher) must define its own version of the role() method.

This hides unnecessary implementation details and enforces a common interface for all person types.

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name):
    
        self._name = name       

    @abstractmethod
    
    def role(self):
    
        pass

2️⃣ Inheritance

The Student and Teacher classes inherit from Person.

They extend the base functionality and provide their specific implementations of the role() method.

This demonstrates how child classes can build upon a parent class.

class Student(Person):

    def __init__(self, name):
    
        super().__init__(name)
        
        self._courses = {}

class Teacher(Person):

    def __init__(self, name):
    
        super().__init__(name)

3️⃣ Encapsulation

Attributes like _name and _courses are encapsulated using a leading underscore to show they are meant for internal use only.

Methods such as set_grade() and view_grades() manage access and modification of these attributes safely.

self._name = name
self._courses = {}


Encapsulation helps protect data and control how it is accessed or modified.

4️⃣ Polymorphism

The function describe(person) can accept any object derived from the Person class.

Regardless of whether person is a Student or Teacher, it correctly calls the role() method specific to that class.

def describe(person):

    print(f"{person._name} is a {person.role()}.")


This shows method overriding and the ability to treat different objects in the same way.

**Demonstration**

teacher = Teacher("Mr. Smith")

student = Student("Chioma")

describe(teacher)

describe(student)

student.enroll("Mathematics")

teacher.assign_grade(student, "Mathematics", "A")

student.view_grades()

**Output**

Mr. Smith is a Teacher.

Chioma is a Student.

Chioma enrolled in Mathematics

Mr. Smith gave Chioma a 'A' in Mathematics

Grades for Chioma:

 - Mathematics: A
