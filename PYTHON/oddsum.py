	#wap to find the sum of all odd terms in a group of nos entered by the user



terms=int(input("enter the number of terms"))
sum=0
while(terms!=0):
    num=int(input("enter the number: "))
    if(num%2!=0):
        sum=sum+num
    terms=terms-1
print("sum of the terms is: ", sum)
    
