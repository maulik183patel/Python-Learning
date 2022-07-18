list1=[10,20,20,30,30,30,40,50,50]
res={}
for i in list(set(list1)):
    res[i]=0
for i in list1:
    res[i]=res[i]+1
#print(res.items)
for key,value in res.items():
    #print(value)
    if value%2==1:
        print(key, end=" ")
    
    #print(key)
