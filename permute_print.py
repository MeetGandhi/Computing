w=input("Enter a word")
l=len(w)
lst=[]
x=""
y=""
"""For a word of 5 letters: We need to create unique nos like abcde where a!=b!=c!=d!=e from 0 to 55555
Then we have to take the corresponding combination of characters"""
for i in range (l):
    x=x+"1"
    y=y+str(l)
ctr=0
m=int(x)
n=int(y)
r=""
for i in range(m,n+1):
    s=str(i)
    for j in range(len(s)):
        if ord(s[j])-48>l or ord(s[j])-48==0:   #Checking for unique numbers
            ctr=1
            continue
        r=r+w[ord(s[j])-49]               #Create string according to unique number
        for k in range (j+1,len(s)):        
            if s[j]==s[k]:
                ctr=1
    for t in range(len(lst)):           #Check for repititions
        if lst[t]==r:
            ctr=1
    if ctr==0 :
        lst.append(r)
    r=""
    ctr=0

print "The combinations of the word are:",lst
