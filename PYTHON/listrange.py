#wap to create a list of nos in the range 1-10 then delete all the even nos from the list and print the final list

num_list=[]
for i in range(1,11):
    num_list.append(i)
print("original list", num_list)

for index, i in enumerate(num_list): #traverse inside the list with both index and value
    if(i%2==0):
        del num_list[index]

print("modified list",num_list)

