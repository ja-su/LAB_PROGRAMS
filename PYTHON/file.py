file=open("file_1.txt","r")
print(file)

print("Name of the file-",file.name)
print("Mode of the file-",file.mode)
print("File closed status before-",file.closed)

#file.write("Hope you are enjoying python")
#file.write("hello")

#lines=["hello world","welcome to python learning","enjoy it"]
#file.writelines(lines)

#print(file.read())

#print("first line-",file.readline())
#print("Second line-",file.readline())
#print("Third line-",file.readline()) 

print(file.readlines())




file.close()
