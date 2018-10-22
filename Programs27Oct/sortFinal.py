lst=[26,3,2,37,2,1,45,30]
N=len(lst)
for n in range(2,N+1):
    x=lst[n-1]
    i=n-2
    while i>=0 and x<lst[i]:
        lst[i+1]=lst[i]
        i-=1
    lst[i+1]=x    

print lst
