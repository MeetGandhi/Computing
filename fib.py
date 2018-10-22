n=input("enter n:")
f=input("enter first term:")
s=input("enter seond term:")
x=[]
x.append(f)
x.append(s)
m=s
print x
for i in range(0,n):
    m=m+x[i]
    x.append(m)
print x

