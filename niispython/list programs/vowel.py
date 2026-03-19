#vowel
s="welcome"
L=[]
for i in s:
	if i in "aeiouAEIOU":
		L.append(i)
print(L)		


s="welcome"
L=[i for i in s if i in "aeiouAEIOU"]
print(L)