#wap that prints the multiple indices of a particular
#value in a list


num_list=[1,2,3,4,5,5,6,4,4,6]
num=int(input("enter the number to be checked"))
i=0
while(i<len(num_list)):
    if(num==num_list[i]):
        print(num,"found at location",i)

ROSHIN RAJESH12:14 PM

list=[1,2,3,4,3,4,5,6]
i=0
m=int(input("Value to be searched :"))

for i in enumerate(list):
    if(list[i] == m):
        print("Number found at location :",i)
