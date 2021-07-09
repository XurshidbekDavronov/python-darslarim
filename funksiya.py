# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:56:24 2021

@author: admin
"""

# def muloqot(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan
#         yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} siz {2020-yosh} da tug'ilgansiz")
# muloqot(ism='olim', yosh=18)

# def kv_kub_hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini 
#     konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2}\n"
#           f"{son} ning kubi {son**3}")
# kv_kub_hisobla(4)

# def juft_toq(son):
#     """Foydalanuvchidan son olib, son juft yoki 
#     toqligini konsolga chiqaruvchi funksiya"""
#     if son%2!=0:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
# juft_toq(4)

# def kattasini_top(son1, son2):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga 
#     chiqaruvchi funksiya. Agar sonlar teng bo'lsa "Sonlar teng" degan 
#     xabar chiqadi."""
#     if son1==son2:
#         print('Bu sonlar teng')
#     elif son1>son2:
#         print(f"{son1} {son2} dan katta")
#     else:
#         print(f"{son2} {son1} dan katta")
# kattasini_top(78, 98)
# kattasini_top(45, 12)
# kattasini_top(56, 56)

# def daraja(x,y):
#     """Foydalanuvchidan x va y sonlarini olib, x ni y darajaga ko'tarib, 
#     konsolga chiqaruvchi funksiya"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")
# daraja(9, 7)

# def daraja(x,y=2):
#     """Foydalanuvchidan x va y sonlarini olib, x ni y darajaga ko'tarib, 
#     konsolga chiqaruvchi funksiya"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")
# daraja(9)

def bolinish_alomati(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha
    bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for i in range(2,11):
        if son%i==0: #if not son%i:
            print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
bolinish_alomati(20)
bolinish_alomati(70)
bolinish_alomati(56)