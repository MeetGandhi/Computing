s=input("enter string:")
lst=list(s)
l=len(s)
i=0
x=0
m=""
for i in range(0,1):
    for x in range(0,l):
        if x!=i and lst[x]==lst[i]:
            m=m
        else:
            m=m+lst[i]
print m
