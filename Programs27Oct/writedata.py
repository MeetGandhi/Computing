# Write data to File
f=open("Input.txt","r")
of=open("Output.txt","w")

header = f.readline() # Does not contain actual info about marks

of.write(header)

for line in f:
    lst=line.split()
    n=len(line)-1
    total=int(lst[2])+int(lst[3]) #int() converts TO integer
    newline=line[:n]+"      "+str(total)+"\n" #str() converts TO string 
    of.write(newline)  
    
f.close()
of.close()

