class Person:
	def f1(self):
		print("Aru is a Person")

class Student(Person):
	def f2(self):
		print("Aru is a Student")

class EngineeringStudent(Student):
	def f3(self):
		print("Aru is a EngineeringStudent")
ob=EngineeringStudent()
ob.f1()
ob.f2()
ob.f3()		
