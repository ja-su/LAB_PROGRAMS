#wap to calculate the exponent of a number using
#recursion

#exp(x,y) = 1, y=0
 #        = x * exp(x ,y-1) otherwise


def exponent(x,y):
    if(y==0):
        return 1
    else:
        return ( x * exponent(x,y-1))

n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
print("result=", exponent(n,m))
     
