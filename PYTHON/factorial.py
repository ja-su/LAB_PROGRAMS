#wap using for loop to calculate the factorial of a number

n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of", n,"is", fact)
