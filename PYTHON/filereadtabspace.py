#wap that accepts file name as input from the user and
#read from the file and calculate the numbner of tabs,
#spaces and newline characterss

filename=input("Enter the filename: ")
with open(filename) as file:
    count_tab=0
    count_space=0
    count_nw=0
    buf=file.read()
    for char in buf:
        if(char=='\t'):
            count_tab+=1
        if(char==' '):
            count_space
