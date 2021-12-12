#wap with class employe that kkeeps track of the number
#of employees in the organization and store the name,
#designation and salary

class employee:
    empcount=0 #class variable
    def __init__(self,name,des,sal):
        self.name=name
        self.des=des
        self.sal=sal
        employee.empcount+=1
    def display(self):
        print("There are %d employees" %employee.empcount)
        print("name= ",self.name,"design= ",self.des, "salary= ",self.sal)
e1=employee("ann","manager",90000)
e2=employee("jeff","tech",98646)#object being created the init method is called
e3=employee("bob","hr",40000)
e4=employee("tom","jre",0000)

e1.display()
e2.display()
e3.display()
e4.display()
