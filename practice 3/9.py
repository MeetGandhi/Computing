n=input("enter n:")
lst=[n]
def collatz(n):
    if n%2==0:
        lst.append(n/2)
        collatz(n/2)
    elif n==1:
        return
    else:
        lst.append(((3*n)+1)/2)
        collatz(((3*n)+1)/2)
collatz(n)
print "The Collatz sequence of",n,"is",lst

