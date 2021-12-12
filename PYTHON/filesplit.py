#wap to split the line in a file into a series of words

with open("file_1.txt","r") as file:
    line=file.readline()
    words=line.split(',')
    print(words)
