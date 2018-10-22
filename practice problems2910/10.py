s=input("enter string:")
lst=list(s)
l=len(lst)
n=0
for i in range(0,l-3):
    if lst[i]=="c" and lst[i+1]=="o" and lst[i+2]=="d" and lst[i+3]=="e":
        n=n+1
    else:
        n=n
print n
