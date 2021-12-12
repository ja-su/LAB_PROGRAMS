#WAP that reads text from a file and writes it into another file
#but in the reverse order

filename = input("Enter the file name: ")

with open(filename) as file1:
    with open("copy.txt","w") as file2:
        for char in reversed(file1.read()):
            file2.write(char)