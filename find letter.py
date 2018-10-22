def find(word,letter):
    i=0
    lst=[]
    for i in range(len(word)):
        if word[i]==letter:
            lst.append(i)
    print lst
word=input("enter the word:")
letter=input("enter the alphabet:")
find(word,letter)

