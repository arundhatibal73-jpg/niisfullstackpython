
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


a=5
b=7
c=3
a=b+c
c=a*3
b=a//4
print(a,b,c)
a=b>c
c=5 or b
b=c>3 and b>7
print(a,b,c)


print(bin(25))
print(oct(25))
print(hex(25))
print(oct(265))
print(hex(265))

print(0b101011)
print(0o27)
print(0xc3)


a=10
b=3
c=a- ~b-1
print(c)



print("enter rectangle length")
l=int(input())
print("enter rectangle breadth")
b=int(input())
ar=l*b
pr=2*(l+b)
print("length",l)
print("breadth",b)
print("area",ar)
print("perimeter",pr)



