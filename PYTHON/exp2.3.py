#factorial of a number using recursion

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n*factorial(n-1))
n=int(input("Enter any number: "))
print("the factorial of ",n,"is",factorial(n))
