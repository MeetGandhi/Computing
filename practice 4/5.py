d2={"a":2,"b":22,"c":222}
d3={'d':3,'e':33,'f':333}
d4={'g':4,'h':44,'i':444}
d5={'j':5,'k':55,'l':555}
d6={'m':6,'n':66,'o':666}
d7={'p':7,'q':77,'r':777,'s':7777}
d8={'t':8,'u':88,'v':888}
d9={'w':9,'x':99,'y':999,'z':9999}
d0={' ':0}
d={"a":2,"b":22,"c":222,'d':3,'e':33,'f':333,'g':4,'h':44,'i':444,'j':5,'k':55,'l':555,'m':6,'n':66,'o':666,'p':7,'q':77,'r':777,'s':7777,'t':8,'u':88,'v':888,'w':9,'x':99,'y':999,'z':9999,' ':0}
s=raw_input("enter the message to be typed:")
lst=list(s)
m=""

for i in range(len(lst)-1):
    if (lst[i] in d2 and lst[i+1] in d2)or(lst[i] in d3 and lst[i+1] in d3)or(lst[i] in d4 and lst[i+1] in d4)or(lst[i] in d5 and lst[i+1] in d5)or(lst[i] in d6 and lst[i+1] in d6)or(lst[i] in d7 and lst[i+1] in d7)or(lst[i] in d8 and lst[i+1] in d8)or(lst[i] in d9 and lst[i+1] in d9)or(lst[i] in d0 and lst[i+1] in d0):
        m=m+str(d[lst[i]])+" "
    else:    
        m=m+str(d[lst[i]])
print m
