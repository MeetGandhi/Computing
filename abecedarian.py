m=""
s=input("enter string:")
lst=list(s)
l=len(s)
lst.sort()
d=""
m=d.join(lst)
if s==m:
    print "true"
else:
    print "false"
