
a=10
b=20
print("before swpping a=",a,"b=",b)

a=a^b
b=a^b
a=a^b
print("after swapping a=",a,"b=",b)

a=10
b=2.5
c="hi"
print(a,b,c)

a=10,2.5,"hi"
print(a)
print(type(a))
print(id(a))
print(id(a))

a=10
b=20
a,b=b,a
print(a,b)

#swapping 3 number left to right with 4th variable
a=2
b=3
c=4
print("before swpping a=",a,"b=",b,"c=",c)
t=c
c=b
b=a
a=t
print("after swapping a=",a,"b=",b,"c=",c)