from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def work(self):
        pass

class Teacher(Person):
    
    def work(self):
        print("Teacher teaches students")

class MathTeacher(Teacher):
    
    def subject(self):
        print("Teaches Mathematics")

obj = MathTeacher()
obj.work()
obj.subject()