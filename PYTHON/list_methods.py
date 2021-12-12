#list method

#append
num_list=[6,3,4,6,8,9,0,6]
num_list.append(10)
print(num_list)

#count
#to count the number a times a number appears on the list
print(num_list.count(6))
print(num_list.count(3))

#index-shows which number appears first
print(num_list.index(6))

#insert-to insert at a particular position
num_list.insert(3,100)
print(num_list)

#reverse
num_list.reverse()
print(num_list)

#sort
sorted(num_list)
print(num_list)