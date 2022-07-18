def getFirstSetBit(n):
    #Your code here
    n=n&(~(n-1))
    cnt=0
    while (n&1)!=1:
        cnt=cnt+1
        n=n>>1
    return cnt+1
print(getFirstSetBit(12))