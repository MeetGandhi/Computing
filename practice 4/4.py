
def permut(s):
    outlist=[]
    if len(s)==1:
        return [s]
    elif len(s)==2:
        outl= [s[0]+s[1], s[1]+s[0]]
        outl.sort()
        return outl
    else:
        for ch in s:
            #print "First character "+ch
            lst=list(s)
            #print "List is: ", lst
            lst.remove(ch)
            #print "List is now: ", lst

            word="".join(lst)
            #print word            
            lst1=permut(word)
            #print lst1
            
            for word1 in lst1:
                outlist.append(ch+word1)
                #print outlist

        st= set(outlist)
        #print st
        out=list(st)
        #print out
        out.sort()
        #print out
        return out
k=""
lst100=[]
lst101=[]
lst102=[]
lst103=[]
lst104=[]
lst105=[]
lst1000=[]
n=input("enter number of dimensions of the vector:")
lst1=[]
lst2=[]
m=""
for i in range(n):
    o=input("enter coordinates of vector-X:")
    lst1.append(o)
for i in range(n):
    p=input("enter coordinates of vector-Y:")
    lst2.append(p)
t1=tuple(lst1)
t2=tuple(lst2)
print "vector-X is",t1
print "vector-Y is",t2
for i in range(n):
    i=str(i)
    m=m+i
lst=permut(m)
for i in range(len(lst)):
    lst3=list(lst[i])
    for j in range(len(lst3)):
        lst100.append(lst1[int(lst3[j])])
for i in range(len(lst)):
    lst3=list(lst[i])
    print lst3
    for h in range(len(lst3)):
        lst101.append(lst2[int(lst3[h])])    
print lst100
print lst101
for g in range((len(lst100))/n):
    lst103=[]
    for t in range(n):
        lst103=lst103+[lst100[(n*g)+t]]
    lst102.append(lst103)
print lst102
for g in range((len(lst101))/n):
    lst104=[]
    for t in range(n):
        
        lst104=lst104+[lst101[(n*g)+t]]
    lst105.append(lst104)
print lst105
for i in range(len(lst102)):
    for j in range(len(lst105)):
        f=0
        for t in range(n):
            f=f+(lst102[i][t]*lst105[j][t])
        lst1000.append(f)
print lst1000
z=min(lst1000)
print "the minimum scalar product of vector-X and vector-Y with all possible permutations of coordinates of respective vectors is",z






    
