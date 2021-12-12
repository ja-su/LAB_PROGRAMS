#wap that takes in the time in hrs and minutes
#aand convertes it into minutes

def convert_time(h,m):
    minutes=h*60+m
    return minutes
hours=int(input("Enter the hours: "))
min=int(input("Enter the minutes: "))
print(convert_time(hours,min))
