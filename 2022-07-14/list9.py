list1 = [5, 10, 15, 20, 25, 50, 20]
list1[0]=1
print(list1)
for i in range(0,len(list1)):
    if list1[i]==20:
        list1[i]=200
print(list1)
