
f=open("/home/students/Desktop/hound.txt","r")
v=f.read()
print "letters:",len(v)
lst=v.split()
print "words:",len(lst)
f.close()
f=open("/home/students/Desktop/hound.txt","r")
c=0
for v in f:
    c=c+1
print "lines:",c 
f.close()
