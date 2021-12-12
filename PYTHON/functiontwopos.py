#write a funtion that accepts two positive numbers m
# and n where m<=n
#return numbers between 1 and n that are divisible by m

def divisible(m,n):
    i=1
    while(i,n):
        if(i%m==0):
            print(i,end="")
        i+=1


m=int(input("enter m"))
n=int(input("enter n"))
divisible(m,n)
