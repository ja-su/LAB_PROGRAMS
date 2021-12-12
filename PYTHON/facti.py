#series 1/1! + 4/2! + 27/3!

def factorial(n):
    f=1
    if(n==0 or n==1):
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
        return f
n=int(input("enter the value of n"))
s=0.0
for i in range(1,n+1):
    s=s+float((i**i)/factorial(i))
print("result=",s)
