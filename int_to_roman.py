def roman(n):
    s=str(n)
    l=len(s)
    lst=list(s)
    lst1=[]
    lst2=[]
    m=""
    for i in range(len(lst)):
        p=int(lst[0])*(10**(len(lst)-1))
        lst1.append(p)
        del lst[0]
    for i in range(len(lst1)):
        if int(lst1[i]) in range(1,4):
            m="I"
            for j in range(int(lst1[i]-1)):
                m=m+"I"
            lst2.append(m)
        elif int(lst1[i])==4:
            m="IV"
            lst2.append(m)
        elif int(lst1[i]) in range(5,9):
            m='V'
            for i in range(int(lst1[i])-5):
                m=m+"I"
            lst2.append(m)
        elif int(lst1[i])==9:
            m="IX"
            lst2.append(m)
        elif int(lst1[i]) in range(10,40):
            m="X"
            f=int(lst1[i])/10
            for j in range(f-1):
                m=m+"X"
            lst2.append(m)
            n=lst1[i]%10
            roman(n)
        elif int(lst1[i]) in range(40,50):
            m="XL"
            lst2.append(m)
            n=lst1[i]%10
            roman(n)
        elif int(lst1[i]) in range(50,90):
            m="L"
            for j in range((int(lst1[i])/10)-5):
                m=m+"X"
            lst2.append(m)
            n=int(lst1[i])%10
            roman(n)
        elif int(lst1[i]) in range(90,100):
            m="XC"
            lst2.append(m)
            n=int(lst1[i])%10
            roman(n)
        elif int(lst1[i]) in range(100,400):
            m="C"
            for j in range((int(lst1[i])/100)-1):
                m=m+"C"
            lst2.append(m)
            n=int(lst1[i])%100
            roman(n)
        elif int(lst1[i]) in range(400,500):
            m="CD"
            lst2.append(m)
            n=int(lst1[i])%100
            roman(n)
        elif int(lst1[i]) in range(500,900):
            m="D"
            for j in range((lst1[i]/100)-5):
                m=m+"C"
            lst2.append(m)
            n=int(lst1[i])%100
            roman(n)
        elif int(lst1[i]) in range(900,1000):
            m="CM"
            lst2.append(m)
            n=int(lst1[i])%100
            roman(n)
        elif int(lst1[i]) in range(1000,10001):
            m="M"
            for j in range((lst1[i]/1000)-1):
                m=m+"M"
            lst2.append(m)
            n=int(lst1[i])%1000
            roman(n)
    d="".join(lst2)
    if d!="":
        print "ROMAN INTEGRAL OF",h,"IS",d
n=input("enter number not exceeding 10000:")
h=n
roman(n)
