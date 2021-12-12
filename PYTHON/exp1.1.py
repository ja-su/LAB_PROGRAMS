l_limit = int(input("Enter the lower limit: "))
u_limit = int(input("Enter the upper limit: "))
print("The prime numbers are:")
for n in range(l_limit,u_limit+1):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)