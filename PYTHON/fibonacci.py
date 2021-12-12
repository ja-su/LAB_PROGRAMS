	#wap to print the fibonnaci series


n=int(input("enter the number of terms: "))
x1=0
x2=1
count=2
print(x1)
print(x2)
while(count<n-2):
    xt=x1+x2
    print(xt)
    x1=x2
    x2=xt
    count+=1
