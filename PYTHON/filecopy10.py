#wap that copies 1st 10 bytes of a file into another.
#opening a file
with open("file_1.txt","rb") as file1:
    with open("file_2.txt","wb") as file2:
        buf=file1.read(10)#reading 10 bytes
        file2.write(buf)#writing onto the file

print("file copied")
