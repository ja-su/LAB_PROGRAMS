#wap to print the sqaure root of the number, if the
#entered value is negative, handle the exception
import math
num=int(input("Enter the number: "))
if(num<0):
    raise Exception("negative value entered")
else:
    ans=math.sqrt(num)
    print("the square root is: ",ans)
