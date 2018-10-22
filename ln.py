def mylog(x,n):
    y=0
    for i in range(1,n+1):
        
        
        
        y=y+(((-1)**(i+1))*((x**i)/i))
    print y
n=input("enter n:")
x=input("enter x:")
mylog(x,n)
