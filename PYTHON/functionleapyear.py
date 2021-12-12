#wap tht contains a funtion is_leap_year() whhich takes
#the year as argument and check whether is leap
#or not

def is_leap_year(year):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
year=int(input("enter any year: "))
is_leap_year(year)
