s=input("enter string:")
l=len(s)
i=0
c=0
r=""
for i in range(0,l):
    for x in range(0,l):
        if x!=i and s[i]==s[x]:
            c=1
    if c==0:
        r=r+s[i]
    c=0
print r
