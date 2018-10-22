s=input("enter string:")
i=0
m=""
for i in range(len(s)):
    if (ord(s[i]) in range(65,91))or(ord(s[i]) in range(97,123)):
        m=m+s[i]
    else:
        m=m
s1=m
def palindrome(s):
    if len(s)==0 or len(s)==1:
        print s1,"is a palindrome"
    elif s[0]==s[-1]:
            palindrome(s[1:-1])
    else:
        print s1,"is not a palindrome"
palindrome(m)
