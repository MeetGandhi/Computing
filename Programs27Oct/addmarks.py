# Cmpute the Total marks
f=open("Input.txt","r")

header = f.readline() # Does not contain actual info about marks
print header.split(),"\n\n\n"
#split() makes a list with individual words
print header

for line in f:
    lst=line.split()
    n=len(line)-1
    total=int(lst[2])+int(lst[3]) #int() converts a string to integer
    newline=line[:n]+"      "
    print newline, total 
    
f.close()

