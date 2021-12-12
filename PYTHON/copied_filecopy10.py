1 #wap that copies 1st 10 bytes of a file into another.
2 #opening a file
3 with open("file_1.txt","rb") as file1:
4     with open("file_2.txt","wb") as file2:
5         buf=file1.read(10)#reading 10 bytes
6         file2.write(buf)#writing onto the file
7 
8 print("file copied")
