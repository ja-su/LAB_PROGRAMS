#wap to copy the entire contents of one file into
#another
with open("file_1.txt","rb") as file1:
    with open("file_2.txt","wb") as file2:
        buf=file1.read()
        file2.write(buf)
print("file copied")
