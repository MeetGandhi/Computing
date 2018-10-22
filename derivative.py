d=input("enter degree of polynomial:")
a=[]
m=""
n=""
for i in range(0,d+1):
    y=input("entercoefficient:")
    a.append(y)
for i in range(0,d+1):
    if i == d:
        m=m+str(a[i])+"x^"+str(i)
    else:
        m=m+str(a[i])+"x^"+str(i)+"+"
print "polynomial is:",m
for i in range(1,d+1):
    if i == d:
        n=n+str(a[i-1]*a[i])+"x^"+str(i-1)
    else:
        n=n+str(a[i-1]*a[i])+"x^"+str(i-1)+"+"
print "derivative is:",n
