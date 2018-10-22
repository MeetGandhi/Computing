s=input("enter the string:")
lst=list(s)
l=len(lst)
i=0
m=""
for i in range(0,l):
    if lst[i] in ["a","e","i","o","u","A","E","I","O","U"]:
        m=m
    else:
        m=m+lst[i]
print m
