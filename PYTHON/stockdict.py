#create a dictionary named stock
#interavtively enter the following elements into the stock
#elements pencils:400, pen:1000, eraser:200, ink:50
#traverse inside the dictionoary and delete the product ink

stock={}
n=int(input("enter the no of products"))
for i in range(n):
    product=input("enter the product name: ")
    value=int(input("enter the value: "))
    stock[product]=value

print(stock)
delete=input("enter the product to delete")
for key in stock:
        del stock[delete]
        break
print(stock)

