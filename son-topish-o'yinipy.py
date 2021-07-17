# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:40:35 2021

@author: admin
"""

"""Sonni topish o'yini"""

import random

def sontop(x=10):
    tasodifiy_son=random.randint(1, x)
    print(f"Men 1 dan {x} gacha bo\'lgan son o\'yladim. Topa olasizmi?")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin=int(input('>>>'))
        if taxmin<tasodifiy_son:
            print('Xato. Men o\'ylagan son bundan katta. Yana harakat qilib ko\'ring.')
        elif taxmin>tasodifiy_son:
            print('Xato. Men o\'ylagan son bundan kichik. Yana harakat qilib ko\'ring.')
        else:
            break
    
    print(f"Tabriklayman!!! Haqiqatda {taxmin} sonini o\'ylagan edim."
          f"{taxminlar} ta taxmin bilan topdingiz")
    return taxminlar
        
def sontop_pc(x=10):
    input(f"1 dan {x} gacha bo\'gan biror sonni o\'ylang, men topaman."
          f"O\'yinni boshlash uchun ENTER tugmasini bosing.")
    quyi=1
    yuqori=x
    taxminlar_pc=0
    while True:
        taxminlar_pc+=1
        if quyi!=yuqori:
            taxmin_pc=random.randint(quyi, yuqori)
        else:
            taxmin_pc=quyi
        javob=input(f"Siz {taxmin_pc} sonini o'yladingiz: to'g'ri (t),"
                    f"men o'ylagan son bundan katta (+) yoki kichik (-)"
                    f"Kerakli tugmani bosing.").lower()
        if javob=='+':
            quyi=taxmin_pc+1
        elif javob=='-':
            yuqori=taxmin_pc-1
        else:
            break 
    print(f"Men {taxminlar_pc} ta taxmin bilan topdim!")
    return taxminlar_pc

def play(x=10):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_pc=sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print(f"{taxminlar_pc} ta taxmin bilan men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"{taxminlar_user} ta taxmin bilan siz yutdingiz!")
        else:
            print("Durang!")
        yana=int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0) ni bosing"))

    
    
