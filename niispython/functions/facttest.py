def facttest():
	print("enter a number")
	no=int(input())
	f=1
	while no>0:
		f=f*no
		no=no-1
	print("factorial=",f)
facttest()





def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number")
no=int(input())
res=facttest(no)
print("factorial=",res)		
