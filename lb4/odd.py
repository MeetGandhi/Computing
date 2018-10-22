s=input("input string:")
l=len(s)
i=0
ch=""
for i in range(0,l):
    if i%2!=0:
        ch=ch+s[i]
    else:
        ch=ch+s[i].capitalize()
print ch
        
