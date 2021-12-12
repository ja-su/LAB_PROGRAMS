#let data represent the list
#["circle","square","triangle"]
#write expressions for the following operations
#1.replace the value circle with ellipse
#2.add a new value rectangle at the top end of list (first element)
#3.remove the values square and traingle from the list

data=["circle","square","traingle"]
print(data)

data[0]="ellipse"
print(data)

data.insert(0,"rectangle")
print(data)

del data[2::]
print(data)