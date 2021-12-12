with open("file_1.txt","r") as file:
    line=file.readline()
    words=line.split(',')
    print(words)

file.close()
