list=[]

num=int(input("Enter the total number of elements to be entered: "))
i=0
while(i<num):
    ip_num=int(input("Enter the number to be inserted to the list: "))
    list.append(ip_num)
    i+=1
print("List: ",list)
search=int(input("Enter the number to be searched: "))
index=list.index(search)
print("The index of the number is: ",index)
