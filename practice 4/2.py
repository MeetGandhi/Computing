c=input("enter the number of credits you received from the local store:")
d=dict()
lst=[]
lst1=[]
m=0
n=input("enter number of all available items in the local store:")
for i in range(n):
    s=input("enter label of the item:")
    lst.append(s)
    w=input("enter credits of the above item:")
    d[s]=w
o=input("enter label of item 1 you want to purchase:")
if o not in lst:
    print "you have entered label item",o,"which is not in the store"
    
p=input("enter label of item 2 you want to purchase:")
if p not in lst:
    print "you have entered label item",p,"which is not in the store"

for j in range(n):
    if lst[j]==o:
        lst1.append(j+1)
        k=j+1
for j in range(n):
    if lst[j]==p:
        lst1.append(j+1)
        s=j+1
lst1.sort()
for i in lst1:
    m=m+d[lst[i-1]]
r=c-m
if r>=0:
    print "after buying items",o,",",p,";",r,"credits is left with you"
    if k<s:
        print "the position of",o,"in the list is",k
        print "the position of",p,"in the list is",s
    else:
        print "the position of",p,"in the list is",s
        print "the position of",o,"in the list is",k
else:
    print "sorry sir you don't have enough credits for purchasing the items",o,p
