n=input("enter number:")
p=n
d=n
l=0
while d!=0:
    d=d/10
    l=l+1
y=0
i=l-1
for i in range(l-1,-1,-1):
    x=n%10
    y=(x*(10**i))+y
    i=i-1
    n=n/10
if y==p:
    print "it is a palindrome"
else:
    print "not a palindrome"
