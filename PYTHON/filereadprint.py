#wap to that reads text from a file and prints only
#those lines that has the word 'print'

filename=input("Enter the file to be read: ")
with open (filename) as file:
    buf=file.read()
    lines=buf.split('\n')
    #print(lines)
    for i in lines:
        if i.find('print', 0, len(i)) != -1 :
            print(i)
    
