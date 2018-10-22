n=raw_input("enter date(format:dd/mm/yy):")
lst=n.split("/")
d=int(lst[0])
m=int(lst[1])
y=int(lst[2])
k=y-(14-m)/12
x=k+k/4-k/100+k/400
j=m+12*((14-m)/12)-2
v=(d+x+(31*j)/12)%(7)
d={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
print n,"falls on",d[v]
