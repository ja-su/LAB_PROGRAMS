#wap to store n numbers into a file input.txt
#read the numbers from the file
#sort the numbers and write it to "output.txt"
#after deleting duplicates

#writing
import pickle

n=int(input("enter the number of elements: "))
file1=open("input.txt","wb")
for i in range(n):
    x=int(input("enter the elements"))
    pickle.dump(x,file1)
file1.close()


#reading
file2=open("input.txt","rb")
list_1=[]
for i in range(n):
    list_1.append(pickle.load(file2))
print(list_1)
file2.close()

#sorting
list_1.sort()
print("Sorted list=",list_1)

#deleting duplicates
list_new=[]
for i in list_1:
    if(i not in list_new):
        list_new.append(i)
print(list_new)

#read file
file3=open("output.txt","wb")
for i in range(len(list_new)):
    pickle.dump(list_new[i],file3)
file3.close()
