s1=input("Enter a string")
s2=input("Enter another string")
s1=s1.upper()
s2=s2.upper()
st1=""
st2=""
l1=len(s1)
l2=len(s2)
for i in range(l1):
    if s1[i]!=' ':
        st1=st1+s1[i]
for j in range(l2):
    if s2[j]!=' ':
        st2=st2+s2[j]        
lst1=list(st1)
lst1.sort()
l1=len(lst1)
lst2=list(st2)
lst2.sort()
l2=len(lst2)
c=1
if l1!=l2:
    c=0
else:
    for i in range(l1):
        if lst1[i]!=lst2[i]:
            c=0

if c==1:
    print "ANAGRAM"
else:
    print "Not an Anagram"
