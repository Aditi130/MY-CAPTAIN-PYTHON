# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:47:14 2022

@author: aditi
"""

# import math module
from math import pi

# take input from user
r = float(input ("Input the radius of the circle : "))

# compute the area from radius of a circle given by user
calculateArea = str(pi * r**2);

#print result
print ("The area of the circle with radius " + str(r) + " is: " + calculateArea)
