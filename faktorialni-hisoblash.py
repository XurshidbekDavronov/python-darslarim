# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:41:39 2021

@author: admin
"""

def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt=fakt*i
        i=i+1
    return fakt
print(faktorial(10))
    