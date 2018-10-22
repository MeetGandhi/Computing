lst=[]
n=input("enter number of elements:")
for i in range(0,n):
    y=input("enter elements:")
    lst.append(y)
    
sortedFlag = 1

for i in range(0,n-1):
    if not (lst[i]<lst[i+1] and lst[n-1]>lst[i]):
        sortedFlag = 0
        break
        #print 'ok'           
    #else:
        #sortedFlag = 0
        #break
        

if sortedFlag == 1:
    print "list is sorted"
else:
    print "list is not sorted"
