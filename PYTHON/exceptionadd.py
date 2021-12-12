#wap that prompts the user to enter two nos and
#displayes their sum
#raise and exception and handle it if a non number value
#is given as input
try:
    num_1=int(input("Enter the first number"))
    num_2=int(input("Enter the second number:" ))
    add=num_1+num_2
    print("sum of the nos: ",add)

except ValueError:
    print("either or one of them or both are not nos:" )
    
