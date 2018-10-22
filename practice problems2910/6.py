s=input("enter string:")
l=len(s)
i=0
m=""
for i in range(0,l):
    if i != l-1 and s[i+1] == ' ':
        m = m + s[i].upper() 
    elif i == l-1:
        m = m+s[i].capitalize()
    else:
        m = m + s[i]
print m    
