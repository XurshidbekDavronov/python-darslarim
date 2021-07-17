# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:39:03 2021

@author: admin
"""

# import math

# uzunlik=lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 1))

# kvadrat=lambda x,y : x**y
# print(kvadrat(3,2))

# def daraja(n):
#     return lambda x: x**n
    
# kvadrat=daraja(2)
# kub=daraja(3)
# print(f"{kvadrat(3)} {kub(2)}")

# from math import sqrt

# sonlar=list(range(0,11))
# # ildizlar=list(map(sqrt, sonlar))
# # print(ildizlar)

# # def daraja2(x):
# #     return x*x

# # print(list(map(daraja2, sonlar)))

# print(list(map(lambda x: x*x, sonlar))) 

# a=[4,5,6]
# b=[7,8,9]
# a_plyus_b=list(map(lambda x,y:x+y, a,b))
# print(a_plyus_b)

import random as r
# sonlar=r.sample(range(100), 10)
# print(sonlar)

# def juftmi(x):
#      return x%2==0

# juft_sonlar=list(filter(juftmi, sonlar))
# print(juft_sonlar)

# juft_sonlar=list(filter(lambda x: x%2==0, sonlar))
# print(juft_sonlar)

mevalar=['olma', 'anjir', 'anor', 'uzum', 'kivi', 'banan', 'o\'rik','ananas']
mevalar2=list(filter(lambda meva:meva.startswith('o'), mevalar))
print(mevalar2)

