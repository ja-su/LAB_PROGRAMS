#wap that reads a file  line by line.
#each line read from the  ffile is copied to another file
#with line numbers specified.
file1=open("filecopy10.py","r")
file2=open("copied_filecopy10.py","w")
lineno=1
for line in file1:
    file2.write(str(lineno) + " " + line)
    lineno+=1

file1.close()
file2.close()
