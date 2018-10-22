n=input("enter n:")
lst=[]
s=0.0
m=0.0
b=0.0
i=0
std=0.0
for i in range(0,n):
    y=input("enter elements(in float):")
    lst.append(y)
i=0
for i in range(0,n):
    s=s+lst[i]
m=s/n
i=0
for i in range(0,n):
    b=b+((lst[i]-m)**2)
std=(b/n)**(1.0/2.0)
print "mean is ",m
print "standard deviation is ",std
