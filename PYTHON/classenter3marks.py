#wap that uses class to store the names and marks of
#the students, Use list to store the marks of 3 subjects

class students:
    def __init__(self,name):#to initialise the variables
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in subject %d-"%(self.name,i+1)))
            self.marks.append(m)
    
    def display(self):
        print(self.name,"got",self.marks)

s1=students("smith") #class instantiation-creating an object called s1
s1.entermarks() #invoking class method through object
s2=students("john")
s2.entermarks()
s1.display()
s2.display()

print(s1 is s2) #false
s2=s1 #aliasing
print(s1 is s2)#true -shallow equality

s1.display()
s2.display()
#s1.name=s2.name #deep equality
