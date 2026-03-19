#delete multiple value using slicing
L=[10,20,30,40,50]
del L[1:3:1]
print(L)

#replacing
L=[10,20,30,40,50]
L[1:3:1]=[15,17]
print(L)


#insert multiple value in list
L=[10,20,30,40,50]
L[1:1:1]=[15,17]
print(L)


L=[10,20,30]
L[1:1:1]=range(5)
print(L)


L=[10,20,30]
L[1:1:1]="hi"
print(L)


L=[10,20,30,40,50]
L[5:5:1]="hi"
print(L)


L=[10,20,30,40,50]
L[-5::1]="hi"
print(L)


L=[10,20,30,40,50]
L[-3:-1:1]="hi"
print(L)





































































