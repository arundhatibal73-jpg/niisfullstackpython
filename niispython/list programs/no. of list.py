L = []
print("Enter how many lists to store:")
s = int(input())

for i in range(s):
    print("Enter list data (comma-separated values):")
    x = input().split(',')  # safer input handling instead of eval
    L.append(x)

print("Elements are:")
for lst in L:
    for elem in lst:
        print(elem, end='\t')
    print()




