class Demo:
	def __init__(self,x,y):
		self.x=10
		self.y=20
print("enter two values")
ob=Demo(int(input()),int(input()))
ob.set(10,20)
print("display first object values")
print(ob.x,ob.y)		