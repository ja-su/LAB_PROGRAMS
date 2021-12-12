ch=input("enter the character")
if(ch.isalpha()):
    print("entered character is an alphabet")
elif(ch.isdigit()):
    print("entered character is a digit")
elif(ch.isspace()):
    print("entered character is a space")
else:
    print("invalid character")
#if-elif-else statement- used for chained conditions
    #else part is optional
