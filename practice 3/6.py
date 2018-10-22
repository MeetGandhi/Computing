lst1=[]
lst2=[]
n=input("enter number of dimensions in vector X and Y:")
for i in range(n):
    t=input("enter element of vector-X:")
    lst1.append(t)
for i in range(n):
    t=input("enter element of vector-Y:")
    lst2.append(t)
print "vector-X=",tuple(lst1)
print "vector-Y=",tuple(lst2)
def calculateEuclidean(lst1,lst2):
    lst=[]
    import math
    for i in range(n):
        m=(lst1[i]-lst2[i])*(lst1[i]-lst2[i])
        lst.append(m)
    res=math.sqrt(sum(lst))
    print "The Euclidean distance between",lst1,"and",lst2,"is",res
calculateEuclidean(lst1,lst2)
