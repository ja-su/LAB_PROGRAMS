#wap using functions to calculate the simple interest
#suppose the customer is a senior citizen then the
#rate of interest is 12% and for all others the rate
#of interest is 10%.

def simple_interest(p,t,s):
    if(s=='y'):
        si=float((p*y*12)/100)
    else:
        si=float((p*y*10)/100)
    return si
p=float(input("Enter the principle amount"))
y=float(input("Enter the number of years"))
sen=input("Enter senior citizenship - y or n")
print("Interest=",simple_interest(p,y,sen))
