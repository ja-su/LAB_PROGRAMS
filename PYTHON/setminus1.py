#wap to read a set of nos until minus one is encountered count the no of positive negative and zeroes entered

neg=pos=zer=0
print("press -1 to exit")
while(1):
    num=int(input("enter the number: "))
    if(num==-1):
        print("exiting......")
        break
    if(num==0):
        zer+=1
    elif(num>0):
        pos+=1
    elif(num<0):
        neg+=1
print("positives are:",pos, "negatives are:",neg, "zeroes are:",zer)
