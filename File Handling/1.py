f=open("/home/students/Desktop/t","r")
while  True:
    v=f.readline()
    if v=="":
        break
    else:
        print v
f.close()
