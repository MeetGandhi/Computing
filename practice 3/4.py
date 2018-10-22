n=input("enter n:")
lst=[]
def rootadd(n):
    import math
    if n==1:
        lst.append(1)
        return
    else:
        lst.append(math.sqrt(n))
        rootadd(n-1)
rootadd(n)
m=sum(lst)
print "Sum of root i from i=1 to",n,"is",m
