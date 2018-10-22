f=""
s=raw_input("enter string(without quotes):")
ls=s.split()
x=0
k=len(ls)
s=""
for x in range(0,k):
    lst=list(ls[x])
    l=len(ls[x])
    i=0
    m=""
    n=""
    for i in range(0,l/2):
        m=lst[i]
        lst[i]=lst[l-1-i]
        lst[l-1-i]=m
        d=""
        f=d.join(lst)
    s=s+f+" "
print s
