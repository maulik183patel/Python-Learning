num=int(input("please enter the number:- \n"))
i=0
while num>0:
    x=int(num%2)
    num=int(num//2)
    print(x,end=" ")
    i=i+1
    print(num)