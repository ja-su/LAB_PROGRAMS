#wap to handle the divide by zero exception

num=int(input("Enter the numberator"))
den=int(input("Enter denominator"))
try:
    quot=num/den
    print("Quotient=",quot)
except ZeroDivisionError:
    print("denominator cannot be zero")
    
