#write a function that accepts three integers and return
#true if any of the integer is 0 otherwise returns false


import time
start=time.time()
def check(x,y,z):
    if(x==0 or y==0 or z==0):
        return 1
    else:
        return 0
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

print(bool(check(a,b,c)))
print(start-time.time())
