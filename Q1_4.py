'''
Q1.4)Write a Python program to find the volume of a sphere with diameter 12 cm.
'''
import math
diameter = 12
r = diameter / 2
v = (4/3) * math.pi * (r ** 3)
print('Volume of sphere is ' +str(round(v, 2)))