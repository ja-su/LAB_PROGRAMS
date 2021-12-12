#wap to count the number of times a particular character appears in a string
st=input("enter the string")
ch=input("enter the character")
count=0
for i in st:
    if(i==ch):
        count+=1
print("The number of times", ch,"appears in", st, "is", count)
    
