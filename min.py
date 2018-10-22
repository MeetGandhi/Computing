def mi(l):
    if len(l)==1:
        return l[0]
    else:
        return min(l[0],mi(l[1:]))
lst=[]
l=input("enter length of list:")
for i in range(l):
    y=raw_input("enter elements of list:")
    lst.append(y)
print "minimum in list",mi(lst)




