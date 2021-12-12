#wap to deposit or withdraw money in  a bank acc

class account:
    def __init__(self):
        self.balance=0
        print("new account created")
    def deposit(self):
        amt=float(input("Enter the amount to be deposited: "))
        self.balance+=amt
        print("New Balance is: ",self.balance)
        

    def withdraw(self):
        amt=float(input("Enter the amount to be withdrawn: "))
        if(amt>self.balance):
            print("Insufficient balance")
        else:
            self.balance-=amt        
            print("New balance is: ",self.balance)

    def enquiry(self):
        print("Balance is: ",self.balance)


ac=account()
ac.deposit()
ac.withdraw()
ac.enquiry()
