s=input("enter string:")
s1=s.upper()
lst=list(s1)
z=0
c=0
h=1
f=1
lst.sort()
l=len(lst)
for h in range(1,l+1):
    f=f*h
i=0
x=0
lst1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lst2=["A","B","C","D","E","F","G","H","I","J","K",'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(0,l):
    for x in range(0,25):
        if lst[i]==lst2[x]:
            lst1[x]=lst1[x]+1
def fac(l):
    z=1
    if l==0:
        z=1
    for i in range(1,l+1):
        z=z*i
    return z
k=0
g=1
for k in range(0,25):
    g=g*fac(lst1[k])
r=(f/g)
print"there are ",r,"possible arrangements" 
            
            
    
