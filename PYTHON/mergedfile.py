#wap that copies 1st 10 bytes of a file into another.
#opening a file
with open("file_1.txt","rb") as file1:
    with open("file_2.txt","wb") as file2:
        buf=file1.read(10)#reading 10 bytes
        file2.write(buf)#writing onto the file

print("file copied")
#wap to compare two files
with open("file_1.txt","r") as file1:
    buf1=file1.read()
with open("file_2.txt","r") as file2:
    buf2=file2.read()
if(buf1==buf2):
    print("same")
else:
    print("not same")
