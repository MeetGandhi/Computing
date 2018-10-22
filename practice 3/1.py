def f(n,k):
    if k==0 or k==n:
        return 1
    else:
        return f(n-1,k-1)+f(n-1,k)
n=input("enter n:")
k=input("enter k:")
if k>n or n<0 or k<0:
    print "invalid input"
else:
    print "the result is:",f(n,k)
