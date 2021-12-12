#wap using function to display a multiplication
#table of n*n size for any given n

def multiplication(n):
    for i in range(1,n+1):
        print(n,"x",i,"=",n*i)
n=int(input("Enter the number"))
multiplication(n)
