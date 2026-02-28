def show():
	x=10
	print("A")
	disp(x)
	print("B")
def disp(x):
    print("C")
    x=30
    print("D")
print("start")
show()
print("end")    	





def show():
	x=10
	print("inside show x=",x)
	disp(x)
	print("inside show x=",x)
def disp(x):
    print("inside disp x=",x)
    x=30
    print("inside disp x=",x)
print("start")
show()
print("end")    