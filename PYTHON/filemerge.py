#wap to merge two files into a third file
filename1=input("Enter the first file name: ")
filename2=input("enter the second file name: ")
filename3=input("Enter the third file name: ")
with open (filename1) as file1:
    with open (filename2) as file2:
        with open (filename3,"w") as file3:
            buf1=file1.read()
            buf2=file2.read()
            buf3=buf1+buf2
            file3.write(buf3)
