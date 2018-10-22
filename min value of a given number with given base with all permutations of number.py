n=input("enter the base of number:")
m=0
k=input("enter the number:")
def permut(s):
    s=str(s)
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
lst2=[]
lst1=permut(k)
for j in range(len(lst1)):
    k=lst1[j]
    c=0
    k=str(k)
    lst=list(k)
    l=len(lst)
    for i in range(l):
        if int(lst[i])<n:
            c=c+1
    if c==l:
        for i in range(l-1,-1,-1):
            m=m+((n**(-i+l-1))*int(lst[i]))
    else:
        print "invalid input"
    lst2.append(m)
x=min(lst2)
print x

