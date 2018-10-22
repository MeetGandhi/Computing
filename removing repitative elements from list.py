l=input("enter number of elements in a list:")
s=[]
for i in range(l):
    y=input("enter element:")
    s.append(y)
print s
j=input("enter element to be removed:")
m=4
n=5
while m!=n:
    m=len(s)
    if j in s:
        s.remove(j)
        n=len(s)

print s
    
