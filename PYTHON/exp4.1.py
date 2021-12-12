file1=input("Enter the file name to be read: ")
file2=input("Enter the new file name: ")
with open (file1) as file_1:
    with open (file2,"w") as file_2:
        buf=file_1.readlines()
        for i in buf:
            if(i!="\n"):
                file_2.write(i)
    
