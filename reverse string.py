s=input("enter the string:")
p=list(s)
l=len(p)
n=l/2
i=0
m=""
for i in range(0,n):
    m=p[i]
    p[i]=p[l-i-1]
    p[l-i-1]=m
d=""
print d.join(p)
