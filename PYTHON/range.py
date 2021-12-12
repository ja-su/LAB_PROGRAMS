#wap to fint the sum of nos in a particular range

x=int(input("enter the starting number of the range"))
y=int(input("enter the ending number of the range"))

s=0
while(x<=y):
    s=s+x
    x=x+1
print(s)
