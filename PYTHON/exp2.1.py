#Find the value of nCr using function

def combination(n,r):
    nCr=factorial(n)/(factorial(n-r)*factorial(r))
    return nCr

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter the value for n: "))
r=int(input("Enter the value for r: "))
print("Value of nCr is: ",combination(n,r))
