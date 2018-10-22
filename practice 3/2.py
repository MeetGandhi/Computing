def palindrome(s):
    if len(s)==0 or len(s)==1:
        print s1,"is a palindrome"
    elif s[0]==s[-1]:
            palindrome(s[1:-1])
    else:
        print s1,"is not a palindrome"
s=input("enter the string:")
s1=s
palindrome(s)
