#wap to find the reverse of a number

num=int(input("enter a number"))
rev=0
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("Reverse of a number is: ",rev)
    
