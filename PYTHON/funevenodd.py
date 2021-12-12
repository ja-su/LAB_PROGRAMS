#wap using function and return statement to check
#whether a given no is even or odd


def even_or_odd(x):
    if(x%2==0):
        return 1
    else:
        return -1
a=int(input("Enter a number: "))
result=even_or_odd(a)
if(result==1):
    print("The number is even")
if(result==-1):
    print("The number is odd")


