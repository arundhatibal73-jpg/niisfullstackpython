print("main Start")
L=[10,20,30]
try:
	print(L[3]//0)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as e:
	print("bye",e)
print("main end")




print("main Start")
L=[10,20,30]
try:
	print(L[2]//0)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as e:
	print("bye",e)
print("main end")




print("main Start")
L=[10,20,30]
try:
	print(L[2]//2)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as e:
	print("bye",e)
print("main end")




print("main Start")
L=None
try:
	print(L[2]//2)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as e:
	print("bye",e)
except:
	print("handle all exception")
print("main end")	