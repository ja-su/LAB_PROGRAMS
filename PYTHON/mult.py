#wap to print the multiplication table of a number entered by the user

n=int(input("enter  the number"))
for i in range(1,11):
    print(n, "x", i, "=", n*i)
