n=input("enter n:")
y=(11**n)-(4**n)
x=y%7
z=y/7
if x==0:
    print"11^n-4^n is divisible by 7"
else:
    print"not divisible"
print "the quotient is ",z
print "the remainder is",x    
