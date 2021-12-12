#wap to print the sum of the series 1/2 + 2/3 + 3/4.....n/n+1
n=int(input("enter the number: "))
s=0.0
for i in range(1,n+1):
    a=float(i)/(i+1)
    s+=a
print(s)
