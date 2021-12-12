print("quadractic equation: a*x^2+b*x+c")
a=int(input("enter a value for a: "))
b=int(input("enter a value for b: "))
c=int(input("enter a value for c: "))

d=(b**2)-(4*a*c)

if(d>0):
    print("there are two roots")
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("first root",r1)
    print("second root",r2)

elif(d==0):
    r3=-b/2*a
    print("only one root: ",r3)
else:
    print("roots are imaginary")
