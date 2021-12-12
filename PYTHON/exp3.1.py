phoneno={}
n=int(input("Enter the number of entries: "))
for i in range(n):
    ph=int(input("Enter the phone number: "))
    name=input("Enter the name of the person: ")
    phoneno[name]=ph
print(phoneno)
for i in sorted(phoneno):
    print(phoneno[i],i)
