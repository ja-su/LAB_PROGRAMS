#wap to create a list of nos in a given range
#then insert the even and odd nos in the list to two
#different lists, say odd and even

num_list=[]
odd=[]
even=[]
m=int(input("Enter the starting range: "))
n=int(input("enter the ending range: "))

for i in range(m,n+1):
    num_list.append(i)
print("original list",num_list)

for i in num_list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list", odd)
