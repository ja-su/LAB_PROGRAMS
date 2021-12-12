#wap that count the number of times a particular character
#appears in a file

with open("file_1.txt","r") as file1:
            buf=file1.readline()

ch=input("Enter the character to be searched: ")
            count=0
            for i in buf:
               # print(ch)

               if(i==ch):
                    count+=1

print("the letter",ch,"appears",count,"times in the file")
