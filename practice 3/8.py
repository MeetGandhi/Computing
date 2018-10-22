p=input("enter first number:")
q=input("enter second number:")
def gcd(p,q):
    if q==0:
        o=p
        return o
    elif p==0:
        o=q
        return o
    elif p>q:
        o=gcd(q,p%q)
        return o
    elif q>p:
        o=gcd(p,q%p)
        return o
if p>=0 and q>=0:
   print "gcd of",p,"and",q,"is",gcd(p,q)
else:
    print "invalid input"
    
     
