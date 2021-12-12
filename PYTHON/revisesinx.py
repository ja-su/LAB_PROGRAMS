#wap to display the values of sin(x) where x ranges from
#0 to 360 degree in steps of 15


#from math import sin
import math
degree=0
while(degree<=360):
    print("sin ",degree,math.sin(math.radians((degree))))
    degree+=15
    
