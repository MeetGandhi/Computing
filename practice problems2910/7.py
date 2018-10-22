i=0
s=[0,1,2,3,4,5,6,7,8,9]
for i in range(0,10):
    s[i]=input("enter string:")
lst=list(s[0])
l=len(lst)
x=0
for x in range(0,l):
    if lst[x] in s[1] and s[2] and s[3] and s[4] and s[5] and s[6] and s[7] and s[8] and s[9]:
        print lst[x]
        
