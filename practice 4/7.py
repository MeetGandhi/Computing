def position(x):
    f=1
    for i in range(len(lst)):
        if lst[i]==x:
            c=i+1
            f=0
            if c==1:
                print "the position i of",x,"in the set S is",c
                print "the number",m,"you entered is pure with respect to set S"
                return 
    
    if f==0:
        print "the position i of",x,"in the set S is",c
        position(c)
         



    else:
        print "element",x,"is not present in the set S"
        print "as a result",m,"is not pure with respect to set S"
n=input("enter no of elements in the set S:")
lst=[]
for i in range(n):
    s=input("enter the elements of set S:")
    lst.append(s)
lst.sort()
st=set(lst)
if len(lst)==len(st):
    print "Set S is",lst
    x=input("enter element of set S whose position is required:")
    m=x
    position(x)
else:
    print "Set S cannot contain repitative elements.Be cautious during input"
    n=input("enter no of elements in the set S:")
    lst=[]
    for i in range(n):
        s=input("enter the elements of set S:")
        lst.append(s)
    lst.sort()
    st=set(lst)
    print "Set S is",lst
    x=input("enter element of set S whose position is required:")
    position(x)
