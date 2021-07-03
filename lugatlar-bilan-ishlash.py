# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:53:48 2021

@author: admin
"""

izohli_lugat = {
    'integer':'butun son',
    'float':"o'nlik son",
    'string':'satr, qator',
    'list':"ro'yhat",
    'tuple':"o'zgarmas ro'yhat",
    'del':"o'chirish",
    'title':'bosh harf bilan chiqarish',
    'upper':'barchasini bosh harfda chiqarish',
    'lower':'barchasini kichik harfda chiqarish'
    }
kalit=input('Kalit sozni kiriting: ').lower()
#print(izohli_lugat.get(kalit, "Bunday so'z yo'q"))
tarjima=izohli_lugat.get(kalit)
if tarjima==None:
    print("Bunday so'z yo'q")
else:
    print(f"{kalit.upper()} -bu {tarjima} ma'nosini anglatadi")
    
