#Consider an employee management system which holds records of employees using dictionaries.(Create dictionary thorughout the program).
#the details contain employee_id, greoos salary and experience. 
# write a program that performs the following operations on the record.
#a. sort the record in ascending order of the gross salary.
#b. print names of the employees with more than 3 years experience.

dict_name = {}
dict_salary = {}
dict_exp = {}

def update_employee():
    i_d = int(input("Enter the employee id: "))
    name = input("Enter the employee name: ")
    salary = int(input("Enter %s's salary: " %(name)))
    exp = int(input("Enter %s's experience: " %(name)))
    dict_name[i_d] = name
    dict_salary[i_d] = salary
    dict_exp[i_d] = exp

def sort_record():
    sort = {}
    for salary in sorted(dict_salary.values()):
        for key, old_salary in (dict_salary.items()):
            if(salary==old_salary):
                sort[key] = salary
    emp_no = 1
    for val, salary in (sort.items()):
        print(emp_no)
        print("Name: ",dict_name[val])
        print("Salary: ", salary)
        print("Experience: ",dict_exp[val])
        emp_no+=1

def emp_exp():
    for val, exp in (dict_exp.items()):
        emp_no = 1
        if (exp>=3):
            print(emp_no)
            print("ID: ",val)
            print("Name: ",dict_name[val])
            print("Salary: ",dict_salary[val])
            print("Experience: ",dict_exp[val])
            emp_no+=1


print("\n-----_____EMPLOYEE MANAGEMENT_____-----")
print("\n\t-----MENU-----")
while(1):
    print("""    1.For updating employees
    2.Sorted record in ascending order of gross salary
    3.Name of employees of over 3 years experience
    4.Exit""")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        update_employee()
    elif(ch==2):
        sort_record()
    elif(ch==3):
        emp_exp()
    else:
        print("EXITING.....")
        break

