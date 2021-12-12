#recursive functions

#find the greatest common divisor of two nos
#largest integer that divides both the nos

#gcd(a,b)=b, if b divides a
#gcd(b,a mod b) otherwise

#a=64

#b=8
#a=62
#b=8
#a/b remainder is zero then b is  gcd

def gcd(a,b):
    rem=a%b
    if(rem==0):
        return b
    else:
        return gcd(b,rem)
m=int(input("Enter the first number"))
n=int(input("Enter the second number"))
print("GCD of two nos",m,"and", n, "is", gcd(m,n))
