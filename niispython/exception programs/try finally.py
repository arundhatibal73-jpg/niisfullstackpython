print("main Start")
L=[10,20,30]
try:
	print(L[2]//2)
finally:	
	print("must execute")
print("main end")	



print("main Start")
L=[10,20,30]
try:
	print(L[2]//2)
except:
	print("handle all exception")
finally:	
	print("must execute")
print("main end")	