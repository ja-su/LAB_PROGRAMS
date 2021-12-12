#wap that prompts the user to enter numbers,
#once the user enters -1 it displays the count, sum
#and average of even numbers and that of odd numbers.

count_even=0
count_odd=0

sum_even=0
sum_odd=0

while(1):
    n=int(input("Enter a number :"))
    if(n==-1):
        break
    if(n%2==0):
        count_even+=1
        sum_even+=n
    else:
        count_odd+=1
        sum_odd+=n
print("Odd count: ",count_odd)
print("Even count: ",count_even)
print("Sum of odd numbers: ",sum_odd)
print("Sum of even numbers: ",sum_even)
print("Average odd: ",sum_odd/count_odd)
print("Average even: ",sum_even/count_even)

