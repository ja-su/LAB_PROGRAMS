#wap to create a dictionary of phone nos and names,
#interactively find out the number of entries in the
#dictionary

#keys are unique (phone number)
#values are phone nos

phoneno_dict={}
n=int(input("Enter the number of entries: "))

for i in range(n):
    phone=int(input("Enter the phone number"))
    name=input("enter the name")
    phoneno_dict[phone]=name
print(phoneno_dict)
