#wap to find the sum of squares of even nos in the range 1 to n

n=int(input("enter the number n: "))
s=0
for i in range(1,n+1):
    if(i%2==0):
        i=(i**2)
        s=s+i
print(s)
        
