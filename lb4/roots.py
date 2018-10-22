a=input("input a:")
b=input("input b:")
c=input("input c:")
d=(b**2)-(4*a*c)
if a==0 and b==0 and c==0:
    print "there are infinitely many roots"
elif a==0 and b!=0 and c!=0:
    print "it is not a quadratic equation"
elif d>=0:
    r=(-b+(d**0.5))/(2.0*a)
    f=(-b-(d**0.5))/(2.0*a)
    print "roots are",r,f
else:
    m=(-b)/(2.0*a)
    n=((-d)**0.5)/(2.0*a)
    r=str(m)+"+"+str(n)+"i"
    f=str(m)+"-"+str(n)+"i"
    print "roots are",r,f
#include more conditions like a=0 b=0 c=0
 
