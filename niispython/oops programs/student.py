class Student:
	def __init__(self,n,r,m):
		self._name=n
		self._roll=r
		self._mark=m
	def show(self):
		print("my name=",self._name)
		print("my roll=",self._roll)
		print("my mark=",self._mark)
s=Student("Aru",1,90.50)
s.show()		