d=input("enter degree of polynomial:")
a=[]
m=0
n=""
for i in range(0,d+1):
    y=input("entercoefficient:")
    a.append(y)
x=input("enter x:")
for i in range(0,d+1):
        m=m+(a[i]*(x**i))
print m
        
