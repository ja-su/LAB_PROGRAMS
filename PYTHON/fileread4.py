#wap that reads a file line by line and prints the four
#letter words in it

file1=open("filecopy10.py","r")

for line in file1:
    for word in line.split():
        if(len(word)==2):
            print(word)
