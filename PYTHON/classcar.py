#create a class car with attributes model,year and price
#and a method cost() for displaying the price

#create two instances of the class and call the method
#for each instance

class car:
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def cost(self):
        print("The cost of the car: ",self.price)

c1=car(input("Enter the model of the car: "),input("enter the year of manufacture: "),int(input("enter the price of the car : ")))
c2=car(input("Enter the model of the car: "),input("enter the year of manufacture: "),int(input("enter the price of the car : ")))

c1.cost()
c2.cost()
