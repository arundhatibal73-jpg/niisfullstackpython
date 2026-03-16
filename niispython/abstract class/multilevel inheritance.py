from abc import *
class Demo(ABC):
	@abstractmethod
	def show():
		pass
class Demo1(Demo):
	def show(self):
		print("hi")
d1=Demo1()
d1.show()		




from abc import *
class Demo(ABC):
	@abstractmethod
	def show():
		pass
	def __init__(self):
		print("constructor")
	def disp(self):
		print("ok")
class Demo1(Demo):
	def show(self):
		print("hi")
d1=Demo1()
d1.show()
d1.disp()		