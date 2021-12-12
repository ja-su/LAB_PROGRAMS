#wap that has a class numbers with values stored in a list
#write the class method called maximum find the largest
#value in the list

class numbers:
    def __init__(self):
        self.values=[]
    def insert_element(self):
        value=int(input("Enter values: "))
        self.values.append(value)
    def maximum(self):
        largest=0
        for i in self.values:
            if(i>largest):
                largest=i
        print("Largest number is: ",largest)

x=numbers()
ch='y'
while(ch=='y'):
    x.insert_element()
    ch=input("You want to enter more elements")


x.maximum()
