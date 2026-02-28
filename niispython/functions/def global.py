x=10#global
def show():
	print(x)
show()
print(x)
	



def show():
	print(x)
	return
x=10#global
show()
print(x)	




x=10#global
def show():
	global x
	x=30
	print(x)#30
	return
show()
print(x)#30	




x=10
def show():
	x=30
	print(x)
	print(globals()['x'])
show()	




