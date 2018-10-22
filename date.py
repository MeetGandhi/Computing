n=raw_input("enter date:")
lst=n.split("/")
mon=[0,"jan","feb","mar","april","may","june","july","aug","sept","oct","nov","dec"]
p=int(lst[1])
q=int(lst[0])
m=int(lst[2])
o=mon[p]
if (p in [1,3,5,7,8,10,12])and(q>=32):
    print "invalid date"
elif (p in [4,6,9,11])and(q>=31):
    print "invalid date"
elif (p==2 and m%4==0 and q>=30) or(p==2 and m%4!=0 and q>=29):
    print "invalid date"
else:
    lm=list(lst[0])
    if lm[1]=="2":
        l="nd"
    elif lm[1]=="1":
        l="st"
    elif lm[1]=="3":
        l="rd"
    else:
        l="th"
    print "date is",lst[0],l,o,"year",lst[2]
