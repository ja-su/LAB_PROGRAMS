 #a book shop contains the details of book titles and
#the number of copies for each title wrtie a menu
#driven program that performs the following operation.

#as the books are added to the shop the number of copies
#shouldd be increased and as the boooks are sold the
#number of copies should decrease


bookshop={}
n=int(input("enter the number of titles: "))
for i in range(n):
    title=input("enter the title of the book: ")
    bookshop[title]=0
print(bookshop)
    
while (True):
    print("1.Add a book")
    print("2.Sell a book")
    print("3.Exit")
    option=int(input("Enter the option"))
    if(option==1):
        title=input("Enter the title of the book: ")
        n=int(input("Enter the number of books to be added: "))
        bookshop[title]+=n
        print(bookshop)
    elif(option==2):
        title=input("Enter the title of the book: ")
        n=int(input("Enter the number of books to be added: "))
        bookshopp[title]-=n
        print(bookshop)
    elif(option==3):
        break
        

