#wap to read a file that contains small case characters
#write these characteres into another file with all
#lower case characters converted into upper case.

filename1=input("Enter the first file name: ")
filename2=input("enter the second file name: ")

with open (filename1) as file1:
    with open (filename2,"w") as file2:
        buf1=file1.read()
        upbuf=buf1.upper()
        file2.write(upbuf)
