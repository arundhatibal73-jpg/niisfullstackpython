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



#insert
L2=[10,2.5,"hi"]
L2.insert(2,30)
print(L2)


#extend
L3=[10,2.5,"hi"]
L3.extend([4,5,6]) #list
print(L3)


#remove
L4=[4,5,10,7,10,8,9]
L4.remove(10)
print(L4)


#pop (remove the last element)
L5=[4,5,8,9]
L5.pop()
print(L5)


#clear (clear all element)
L6=[4,5,8,9]
L6.clear()
print(L6)


#sort 
L7=[4,10,8,3]
L7.sort()
print(L7)


#reverse
L8=[4,5,8,9]
L8.reverse()
print(L8)


L8=[4,3,7,9]
L8.sort(reverse=True)
print(L8)



#count
L9=[2,4,6,2,9]
print(L9.count(4))



#copy
L10=[3,5,8,1]
L1=L10.copy()
L1.append(40)
print(L10)
print(L1)


#index
L11=[3,6,7,4,9]
print(L11.index(6))









