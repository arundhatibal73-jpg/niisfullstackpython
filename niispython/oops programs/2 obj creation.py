#2 object creation#
class Demo:
	def __init__(self):
		self.x=10
		self.y=20
ob=Demo()
print(ob.x)
ob1=Demo()
print(ob1.x)
print(ob1.y)



class Demo:
	def __init__(self):
		self.x=10
		self.y=20 #instance variable
ob=Demo()
print(ob.x)
print(ob.y)




class Demo:
	def __init__(self):
		print("enter two values")
		self.x=int(input())
		self.y=int(input())
print("enter object1 & values")
ob=Demo()
print("enter oblect2 & values")
ob1=Demo()
print("display first object values")
print(ob.x,ob.y)
print("display second object values")
print(ob1.x,ob1.y)		