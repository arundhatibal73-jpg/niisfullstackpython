#even no.+3
L=[5,8,6,3,8,7,7,12]
L1=[i+3 for i in L if i%2==0]
print(L1)

#odd no.+3
L=[5,8,6,3,8,7,7,12]
i=0
while i<len(L):
	if L[i]%2!=0: #if add-->remove
		L.remove(L[i])
	else:
		i+=1 #move only if not removed
print(L)		