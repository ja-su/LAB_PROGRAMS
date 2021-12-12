#wap to create a class person with attributes name and age.two classes ,namely
#student and teacher inherits the person class. write methods in the derived
#classes toprint the general and specific details. add specific details
#as necessary

class person:
    def _init_(self,name,age):
        self.name =name
        self.age=age

    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)

class teacher(person):
    def _init_(self,name,age,exp,sub):
        person._init_(self,name,age)
        self.exp=exp
        self.sub=sub

    def displaydata(self):
        person.display(self)
        print("expierence : ",self.exp)
        print("subject taught : ",self.sub)

class student(person):
    def _init_(self,name,age,marks):
        person._init_(self,name,age)
        self.marks=marks

    def displaydata(self):
        person.display(self)
        print("marks : ",self.marks)
    
        

t=teacher("saritha",42,15,"python")
t.displaydata()
        
s=student("emmu",20,50)
s.displaydata()
