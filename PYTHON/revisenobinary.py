#wap to read a integer. If it is positive then
#display the corresponding binary representation of
#that number. the user enters 999 to stop.
#in case a negative number is enterd ask the user to
#re-enter a positive number


while(1):
    num=int(input("Enter a number: "))
    if(num<0):
        print("Negative number entered!!")
        print("Please re-enter the number")
    elif(num==999):
        break
    else:
        print(bin(num))
        
