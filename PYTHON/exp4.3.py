class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def showData(self):
        print("The name of the student is: ",self.name)
        print("The roll number of the student is: ",self.rollno)
        
s1=student("Jake",37)
s2=student("Tony",66)

s1.showData()
s2.showData()
