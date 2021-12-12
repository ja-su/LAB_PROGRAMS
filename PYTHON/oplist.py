#operations on list

list_1=[1, 2, 3,4, 5, 6, 7, 8, 9, 10]
list_2=[1, "abcd", 'g', 0]
#list_2=list_1
#print(list_2)


list_3=list_1[2:6]
#print(list_3)

#maximum and minimum
#print(max(list_1))
#print(min(list_1))

#print(len(list_1))
#print(len(list_2))

list_3=list_1+list_2
print(list_3)
#count the number of times an element appears in a list
#print(list_3.count(1))


#print(list_3.index("abcd"))
print(list_3.index(1))


#reverse the list
list_3.reverse()
print(list_3)

#sort the list


list_4=[34,6,78,900,12000,4,3,567]
print(list_4)
list_4.sort()
print(list_4)

#insertion into the list

list_4.insert(1,2000)
print(list_4)

#removal from list
list_4.pop(4)
print(list_4)
