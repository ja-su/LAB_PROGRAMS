#create  a stock database using dictionaries.(create a disctionary through the program).
#the database holds records, which contan item name, number of units and rate per unit. 
#write a program that performs the following
#a. updatin the stock details.
#b. printing the stock details.
#c. sorting the databse based on the number of units.

stock = []

def add_item():
    item = {}
    item["name"] = input("Enter the name of item: ")
    item["units"] = int(input("Enter the number of units: "))
    item["rate"] = int(input("Enter the rate per unit: "))
    stock.append(item)

def update_item():
    name = input("Enter the name of the item: ")
    for i in stock:
        if(i["name"]==name):
            i["units"] = int(input("Enter the number of units: "))
            i["rate"] = int(input("Enter the rate per unit: "))
            input("Update complete. press any key to continue")
            return
    print("Item not found")

def display_sort():
    for i in sorted(stock, key = lambda x: x["units"]):
        print("""\nName : {i["name"]}
        Number of units : {i["units"]}
        Rate per unit   : {i["rate"]}""")


print("""-----MENU-----
1.Add a new item
2.Update an item
3.Sort and display
4.Exit""")
while(True):
    ch = int(input("Enter the choice: "))
    if(ch==1):
        add_item()
    elif(ch==2):
        update_item()
    elif(ch==3):
        display_sort()
    else:
        print("EXIT")
        break