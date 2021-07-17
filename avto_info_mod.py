# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:11:52 2021

@author: admin
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rangi': rangi,
          'korobka':korobka,
          'yil':yili,
          'narh':narhi}
    return avto

def avto_kirit():
    print('Saytimizdafi avtomobillar ro\'yhatini shakllantiramiz.')
    avtolar=[]
    while True:
        print('\nQuyidagi ma\'lumotlarni kiriting', end='')
        kompaniya=input('Ishlab chiqaruvchi:')
        model=input('Modeli:')
        rangi=input('Rangi:')
        korobka=input('Korobka:')
        yili=input('Ishlab chiqarilgan yili:')
        narhi=input('Narhi:')
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        javob=input('Yana avtomobil qo\'shasizmi? (yes/no):')
        if javob=='no':
            break
    return avtolar
    
def info_print(avto_info):
    print('\nSalonimizdagi avtomobillar:')
    print(f"{avto_info['rangi'].title()} {avto_info['model']} {avto_info['yil']} -yil" 
          f" Narhi:{avto_info['narh']}")
    
