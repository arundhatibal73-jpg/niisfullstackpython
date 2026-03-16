print("main Start")
L=[10,20,30]
print(L[2])
print("main end")

'''0=10
   1=20
   2=30'''



print("main Start")
L=[10,20,30]
try:
	print(L[3])
except IndexError as e:
	print(e)
print("main end")