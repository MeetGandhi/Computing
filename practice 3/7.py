lst=[]
n=input("enter number of elements in one dimensional array of floats:")
for i in range(n):
    h=input("enter element of one dimensional array of floats:")
    lst.append(h)

def reversearray(lst):
    print "the one dimensional array of floats you entered is",lst
    for i in range(len(lst)/2):
        m=lst[-1-i]
        lst[-1-i]=lst[i]
        lst[i]=m
    print "the one dimensional array of floats in reversed order is",lst
reversearray(lst)

    
