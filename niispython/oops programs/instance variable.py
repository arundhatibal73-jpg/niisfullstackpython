class Demo:
	def __init__(self,x,y):#method
		self.x=x #public instance variable
		self.y=y #instance variable
ob=Demo(10,20)
print(ob.x,ob.y)		




class Demo:
	def __init__(self,x,y):#method
		self.x=x #public instance variable
		self._y=y #private instance variable
ob=Demo(10,20)
print(ob.x,ob._y)