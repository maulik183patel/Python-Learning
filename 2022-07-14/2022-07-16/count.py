num=int(input("enter the number\n"))
#l=int(len(num))
count=0
while num>0:
    num=num//10
    count+=1
    print(count)