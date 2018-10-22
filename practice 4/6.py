def position(x):
    f=1
    for i in range(len(lst)):
        if lst[i]==x:
            c=i+1
            f=0
    if f==0:
        print "the position i of",x,"in the set S is",c
    else:
        print "element",x,"is not present in the set S"
n=input("enter no of elements in the set S:")
lst=[]
for i in range(n):
    s=input("enter the elements of set S:")
    lst.append(s)
lst.sort()
st=set(lst)
if len(lst)==len(st):
    print "Set S is",lst
    x=input("enter element of set S whose postion is required:")
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
    x=input("enter element of set S whose postion is required:")
    position(x)
