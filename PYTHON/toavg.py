a=int(input("enter the mark of the first subject: "))
b=int(input("enter the mark of the second subject: "))
c=int(input("enter the mark of the third subject: "))
d=int(input("enter the mark of the forth subject: "))

total=a+b+c+d
avg=total/4

if(avg>=90):

    print("GRADE: O")
elif(avg>=80 and avg<90):
    print("GRADE: A+")
elif(avg>=70 and avg<80):
    print("GRADE: A")
elif(avg>=60 and avg<70):
    print("GRADE: B")
elif(avg>=50 and avg<60):
    print("GRADE: C")
else:
    print("GRADE: F")
