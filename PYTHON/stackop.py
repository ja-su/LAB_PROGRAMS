#operations on stack

stack_list=[]
print("Originall stack is",stack_list)

for i in range(1,11):
    num=int(input("enter the element to be pushed"))
    stack_list.append(num)
    print("stack after push",stack_list)
print("final stack list is: ",stack_list)

for i in range(1,6):
    stack_list.pop()
    print("stack after pop",stack_list)
