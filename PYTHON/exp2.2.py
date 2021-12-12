#Implement a calculator using functions

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def exp(x,y):
    return x**y

print("Enter the operation to be performed: ")
print("1.Additon")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")

while True:
    ch=int(input("Enter your choice: "))
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second numbre: "))
    if(ch==1):
        print(num1,"+",num2,"=",add(num1,num2))

    elif(ch==2):
        print(num1,"-",num2,"=",sub(num1,num2))
    elif(ch==3):
        print(num1,"*",num2,"=",mul(num1,num2))
    elif(ch==4):
        print(num1,"/",num2,"=",div(num1,num2))
    elif(ch==5):
        print(num1,"^",num2,"=",exp(num1,num2))
    else:
        print("!!Entered option is invalid!!")
