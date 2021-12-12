num=int(input("Enter the number"))
reverse=0
temp=num
while(num>0):
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
if(temp==reverse):
    print("the given number is palindrome")
else:
    print("the given number is not palindrome")
