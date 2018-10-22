lst=[]
for i in range(5):
    s=input("enter number:")
    if s%2!=0:
        lst.append(s)
if len(lst)==0:
    print "no odd number entered"
else:
    m=max(lst)
    print "largest odd number from the entered numbers is",m
