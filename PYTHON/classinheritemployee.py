#wap to create a class named :member having the following
#data members
#name,age,phoneno,addr,salary.It also have a method
#named "printsalary" which prints the salary of the
#members.

#two classes "employee" and ,"manager" inheris the "member"
#the "eemployee" and "manager" classes have  data membrs
#like specialisatoins and department respectively
#now asssign name,age,phoneno,addr,salary to an employee
#and a manager by making an object of both of these classes and
#print the same

class member:
    def __init__(self,name,age,phoneno,addr,sal):
        self.name=name
        self.age=age
        self.phoneno=phoneno
        self.addr=addr
        self.sal=sal
    def display(self):
        print("name:",self.salary)
        print("age:",self.age)
        print("phone number:",self.phoneno)
        print("address:",self.addr)
    def salary(self):
        print("salary:",self.sal)
class employee(member):
    def _init_(self,specialization):
        self.specialization=specialization
    def disp(self):
        print("specialization:",self.specialization)
class manager(member):
    def _init_(self,department):
        self.department=department
    def dis(self):
        print("department:",self.department)


m=member(input("enter name :"),int(input("enter age:")),int(input("enter phone number")),input("enter address"),int(input("enter salary")))
m.display()
m.salary()
e=employee(input("enter specialisation"))
e.disp()
man=manager(input("enter department"))
man.dis()
