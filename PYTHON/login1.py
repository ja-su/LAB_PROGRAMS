def register():
    flag=0
    key=input("Enter username: ")
    val=input("Enter password: ")  
    file1 = open("users.txt","r")
    verify = file1.read()
    if (key + " " + ":" + val) in verify:
        print("User exists!")
    elif (key) in verify:
        print("User exists!")
    else:
        file1.close()
        file1 = open("users.txt","a")
        file1.write(key + " " + ":" + val + "\n")
        print("Registration successful")
    file1.close()

def login():
    key=input("Enter username: ")
    val=input("Enter password: ")
    file2 = open("users.txt", "r")
    verify = file2.read()
    if (key + " " + ":" + val) in verify:
        print("Login Success")
    elif (key) in verify:
        print("Password not recognised")
    else:
        print("User not found")
    file2.close()
while(1):
    print("1.Create a user")
    print("2.Login")
    print("3.Exit")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        register()
    elif(ch==2):
        login()
    elif(ch==3):
        break 
    else:
        print("invalid entry")
