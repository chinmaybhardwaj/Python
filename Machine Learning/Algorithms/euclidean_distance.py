# -*- coding: utf-8 -*-

from math import sqrt

point1 = [1,3]
point2 = [2,5]


euclidean_dist = sqrt( ((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2) )

print(euclidean_dist)
