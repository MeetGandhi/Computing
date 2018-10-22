s1=input("enter string1:")
s2=input("enter string2:")
lst1=list(s1)
lst2=list(s2)
l1=len(lst1)
l2=len(lst2)
m=""
if l1==l2:
    for i in range(0,l1):
        m=m+lst1[i]
        m=m+lst2[i]
else:
    if l1>l2:
        for i in range(0,l2):
            m=m+lst1[i]+lst2[i]
    else:
        for i in range(0,l1):
            m=m+lst1[i]+lst2[i]
print m
