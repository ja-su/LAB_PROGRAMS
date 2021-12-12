#wap using function that computes the area and volume of
#a sphere

import math
def sphere(r):
    area=4*math.pi*r**2
    vol=(4/3)*math.pi*r**3
    print("Area of sphere: ",area)
    print("Volume of the sphere: ",vol)







r=int(input("Enter the radius: "))
sphere(r)

