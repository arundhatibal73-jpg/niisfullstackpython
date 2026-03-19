#append
L1=[]
L1.append(10)
L1.append(2.5)
L1.append("hi")
print(L1)

L1=[10,2.5,"hi"]
print(L1)


L1=[10,2.5,"hi"]
L1.append(30)
print(L1)



L=[5,8,6,3,8,7,7,12]
L1=[]
for i in L:
	if i not in L1:
		L1.append(i)
print(L1)	


L=[5,8,6,3,8,7,7,12]
L1=[i for i in L]
print(L)
