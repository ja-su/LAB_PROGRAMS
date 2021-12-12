#write a class rectangle that has attributes length and
#bredth. Also write a method area which returns the
#area of the rectangle

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth

rect=rectangle(int(input("Enter the length of the rectangle: ")),int(input("Enter the breadthe of the rectangle: ")))
print("area : ",rect.area())
