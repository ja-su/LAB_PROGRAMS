list=[]
num=int(input("Enter the size of the list: "))
sum=0
avg=0
print("Enter the elements to the list: ")
for i in range(0,num):
    number=int(input())
    list.append(number)
print("Original List",list)
print("Squares of each number in the list:")
for j in list:
    sum+=j
    square=j**2
    print(square)

avg=sum/num
print("The average of the numbers are: ",avg)

