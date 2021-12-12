#wap that has a class cirle
#use class variable to define the value of pi
#use this class variable to find the area and
#circumference of the circle

class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi * self.radius * self.radius
    def circumference(self):
        return 2 * circle.pi * self.radius
c=circle(5.0)
print("area= ",c.area())
print("circumference= ",c.circumference())
