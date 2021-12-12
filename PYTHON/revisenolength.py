#wap that accepts any number and prints the number of
#digits in that number

num=int(input("Enter the number: "))
count=0
n=num
while(num!=0):
    count+=1
    num=int(num/10)

print("Number of digits in",n,"is",count)
    
