lst=[3,5,9,10,11,8]
n=len(lst)
x=lst[n-1]
#----------------
i=n-2
while i>=0 and x<lst[i]:
    lst[i+1]=lst[i]
    i-=1

lst[i+1]=x    
#----------------
print lst
# [3, 5, 8, 9, 10, 11]
