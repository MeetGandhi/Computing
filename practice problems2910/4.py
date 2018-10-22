s1=input("enter string1:")
s2=input("enter string2:")
lst=list(s1)
l=len(s1)
i=0
m=""
for i in range(0,l):
    if lst[i] in s2:
        m=m
    else:
        m=m+lst[i]
print m
