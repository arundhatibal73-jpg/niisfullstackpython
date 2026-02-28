x=10#global
def show():
	x=30#local
	print(x)#30
show()
print(x)#10



x=10
def show():
	x=30
	print(x)#30
	print(locals()['x'])#30
	print(globals()['x'])#10
show()




x=10
def show():
	x=30
	print(x)#30
	print(locals()['x'])#30
	print(globals()['x'])#10
	globals()['x']=50
	x=60
show()
print(x)    
