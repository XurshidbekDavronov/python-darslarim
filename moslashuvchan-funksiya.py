# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:55:43 2021

@author: admin
"""

# def kopaytma(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# natija=kopaytma(5,6)
# print(natija)

# def kopaytma(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# natija=kopaytma(5,6)
# print(natija)

def talaba_haqida(ism, familiya, **malumot):
    malumot['ism']=ism
    malumot['familiya']=familiya
    return malumot

talaba=talaba_haqida('xurshid', 'davronov', yosh=35, kurs=4, fakultet='tillar')   
print(talaba)
