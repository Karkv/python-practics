import math 

from math import pi



h=float(input("h=="))
r=float(input("r=="))

circles=2*(pi*r**2)
side=2*pi*r*h
area=circles+side

print("A=",round(area,2))