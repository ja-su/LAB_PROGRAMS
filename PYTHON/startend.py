#wap using for loop to print all the numbers from m to n and classify them as even  or odd

m=int(input("enter the starting number: "))
n=int(input("enter the ending number: "))
for i in range(m, n+1):
    if(i%2==0):
        print(i, "is an even number")
    else:
        print(i, "is an odd number")
        
