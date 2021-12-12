#wap to compare two files
with open("file_1.txt","r") as file1:
    buf1=file1.read()
with open("file_2.txt","r") as file2:
    buf2=file2.read()
if(buf1==buf2):
    print("same")
else:
    print("not same")
