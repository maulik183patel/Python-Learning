list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]
for i in list1:
    for j in list2:
        z=list(i+j)
        list3=list3+z
        print(z)
        print(z, end=" , ")