#wap to classify the given number as prime number  or a composite number

num=int(input("enter the number: "))
composite_flag=0
for i in range(2,num):
    if(num%i==0):
        composite_flag=1
        break
if(composite_flag==1):
    print("composite number")
else:
    print("prime number")
