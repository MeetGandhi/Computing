s=input("enter string:")
i=0
m=""
for i in range(len(s)):
    if (ord(s[i]) in range(65,91))or(ord(s[i]) in range(97,123)):
        m=m+s[i]
    else:
        m=m
print m
