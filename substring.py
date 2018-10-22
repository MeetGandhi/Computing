s1=input("enter the first string:")
s2=input("enter the second string:")
lst1=list(s1)
l1=len(s1)
lst2=list(s2)
l2=len(s2)
i=0
x=0
c=0
j=0
for i in range(0,l1):
        if lst1[i]==lst2[i]:
            c=c+1
            j=j+1
        else:
            c=0
            j=j+1
if c==l1:
    print s1,"is a substring of",s2
else:
    print s1,"is not a substring of",s2
