#count char modified
st=input("enter the string")
ch=input("enter the character")
count=0
index=0
for i in st:
    print(i)
    if(i==ch):
        count+=1
        
print("The number of times", ch,"appears in", st, "is", count)
