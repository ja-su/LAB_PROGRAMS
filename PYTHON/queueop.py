#queue operations

queue=[]
print("The original queue list is",queue)

for i in range(1,6):
    num=int(input("enter the element to be pushed"))
    queue.append(num)
    print("queue after push operation")
print("final queue is: ",queue)

for i in range(1,6):
    queue.pop(0)
    print("queue after pop",queue)
