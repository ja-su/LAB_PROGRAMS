#write a python program to store
#the prime nos between m and n in a list

list = []
def prime(m,n):
    for n in range(m,n):
        if(n>1):
            for i in range(2,n):
                if(n%i==0):
                    break
            else:
                print(n)






m = int(input("Enter the starting range: "))
n = int(input("Enter the ending range: "))

print("Prime nos are: ", prime(m,n))