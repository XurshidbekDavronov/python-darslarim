# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:15:50 2021

@author: admin
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
    
    def get_name(self):
        return self.ism
    
    def get_age(self, yil):
        return yil-self.tyil
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya} tug'ilgan yilim {self.tyil}"
        
    

talaba1=Talaba('Olim', 'Olimov', 2000)
talaba2=Talaba('Ali', 'Soliyev', 1999)
talaba3=Talaba('Sobir', 'Nosirov', 2001)
print(talaba1)
 