#wap that promts a user to enter a string
#the program calculates and displayes the length of the
#string until the user enters "quit".

while 1:
    
    string=input("Enter the string: ")
    if(string=="QUIT"):
        break
    else:
        print(len(string))
