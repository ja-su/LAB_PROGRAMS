#wap to print the prime factors of a number


def prime(x):
    flag_composite=0
    for i in range(2,x):
        if(x%i==0):
            flag_composite=1
            break
    return flag_composite

num=int(input("Enter a number: "))
i=2
while(i<=num/2):
    if(num%i==0):
        if(prime(i)==0):
            print(i,end=' ')
    i+=1
    
