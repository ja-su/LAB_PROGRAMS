#model exam- ques 1

dict = {}
n = int(input("Enter the number of entries: "))
for i in range(n):
    dob = int(input("Enter the date of birth in dd-mm-yy format: "))
    name = input("Enter the name: ")
    dict[name] = dob
print(sorted(dict.items()))

choice = 'y'

while(choice=='y'):
    check_name = input("Enter the name to check: ")
    if(check_name in dict.keys()):
        print("Name is present")
    
    else:
        print()
        print("Name not present")
        print("Please enter the details...")
        dob = int(input("Enter the dob in dd-mm-yy  format: "))
        name = input("Enter the name: ")
        dict[name] = dob
        print(sorted(dict.items()))
        choice = input(("DO YOU WANT TO CONTINUE y or n: "))