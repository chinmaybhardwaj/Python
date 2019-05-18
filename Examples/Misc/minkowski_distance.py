# Python3 program to find Minkowski distance 
  
# import math library 
from math import *
from decimal import Decimal 
  
# Function distance between two points  
# and calculate distance value to given 
# root value(p is root value) 
def p_root(value, root): 
      
    root_value = 1 / float(root) 
    return round (Decimal(value) **
             Decimal(root_value), 3) 
  
def minkowski_distance(x, y, p_value): 
      
    # pass the p_root function to calculate 
    # all the value of vector parallely  
    return (p_root(sum(pow(abs(a-b), p_value) 
            for a, b in zip(x, y)), p_value)) 
  
# Driver Code 
vector1 = [22, 6, 42, 10, 62] 
vector2 = [27, 16, 32, 6, 64] 
p = 3
print(minkowski_distance(vector1, vector2, p))