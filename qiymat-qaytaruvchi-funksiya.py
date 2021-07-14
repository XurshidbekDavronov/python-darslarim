# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 09:14:03 2021

@author: admin
"""

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism yasash funksiyasi"""
#     toliq_ism=f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# talaba=toliq_ism_yasa('olim', "Olimov")
# print(talaba)

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism yasash funksiyasi"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1=toliq_ism_yasa('olim', "Olimov", 'Hakimovich')
# talaba2=toliq_ism_yasa("sobir", 'soliyev')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={'kompaniya':kompaniya,
#          'model':model,
#          'rangi': rangi,
#          'korobka':korobka,
#          'yil':yili,
#          'narh':narhi}
#     return avto

# avto1=avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020)
# avto2=avto_info('GM', 'Lacetti', 'oq', 'avtomat', 2019, 15000)
# avtolar=[avto1, avto2]
# print('Bozordagi mashinalar narhi:')
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Belgilanmagan'
#     print(f"{avto['rangi'].title()} {avto['model']} {avto['yil']} -yil Narhi:{narh}")

        
# def oraliq(min, max, qadam=None):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             min+=qadam
#         else:
#             min+=1
#     return sonlar

# print(oraliq(100, 111,5))
# print(oraliq(0, 20,3))

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={'kompaniya':kompaniya,
#           'model':model,
#           'rangi': rangi,
#           'korobka':korobka,
#           'yil':yili,
#           'narh':narhi}
#     return avto
# print('Saytimizdafi avtomobillar ro\'yhatini shakllantiramiz.')
# avtolar=[]
# while True:
#     print('\nQuyidagi ma\'lumotlarni kiriting', end='')
#     kompaniya=input('Ishlab chiqaruvchi:')
#     model=input('Modeli:')
#     rangi=input('Rangi:')
#     korobka=input('Korobka:')
#     yili=input('Ishlab chiqarilgan yili:')
#     narhi=input('Narhi:')
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob=input('Yana avtomobil qo\'shasizmi? (yes/no):')
#     if javob=='no':
#         break
# print('\nSalonimizdagi avtomobillar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Belgilanmagan'
#     print(f"{avto['rangi'].title()} {avto['model']} {avto['yil']} -yil Narhi:{avto['narh']}")

        
# def foydalanuvchi(ism, familiya, t_yil, t_joyi, telefon=None, email=''):
#     mijoz={'ism':ism,
#           'familiya':familiya,
#           't_yil': t_yil,
#           't_joyi':t_joyi,
#           'telefon':telefon,
#           'email':email}
#     return mijoz
# print('Saytimizdan foydalanuvchilarning ro\'yhatini shakllantiramiz.')
# mijozlar=[]
# while True:
#     print('\nQuyidagi ma\'lumotlarni kiriting', end='')
#     ism=input('Ismingizni kiriting:')
#     familiya=input('Familiyangizni kiriting:')
#     t_yil=int(input('Tug\'ilgan yilingiz:'))
#     t_joyi=input('Tug\'ilgan joyingiz:')
#     telefon=input('Telefon raqamingiz (agar bor bo\'lsa):')
#     email=input('Elektron pochta manzilingiz(agar bor bo\'lsa):')
#     mijozlar.append(foydalanuvchi(ism, familiya, t_yil, t_joyi, telefon, email))
#     javob=input('Yana foydalanuvchi qo\'shasizmi? (yes/no):')
#     if javob=='no':
#         break
# print('\nSaytimizdagi mijozlar:')
# for mijoz in mijozlar:
#     if mijoz['telefon']=='':
#         telefon='yo\'q'
#     else:
#         telefon=mijoz['telefon']
#     if mijoz['email']=='':
#         email='yo\'q'
#     else:
#         email=mijoz['email']
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, Manzili {mijoz['t_joyi'].title()}",
#           f"yoshi {2021-mijoz['t_yil']} da, Telefon raqami: {mijoz['telefon']};",
#           f"Elektron pochta manzili: {mijoz['email']}.")

# def kattasi(x, y, z):
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max
# maks=kattasi(12, 12, 12)
# print(maks)

# def aylana_info(radius, PI=3.14):
#     aylana={'radius': radius,
#          'diametr': 2*radius,
#          'perimetr': 2*PI*radius,
#          'yuza':PI*radius**2}
#     return aylana
# rad1=aylana_info(5)
# rad2=aylana_info(45)
# radiuslar=[rad1, rad2]
# for aylana in radiuslar:
#     print(f"\n Aylana radiusi: {aylana['radius']};\nAylana diametri:" 
#       f"{aylana['diametr']}"
#       f"\nAylana perimetri: {aylana['perimetr']}"
#       f"\nAylana yuzasi:{aylana['yuza']}")

# def oraliq(min, max):
#     tub_sonlar=[]
#     for n in range(min, max+1):
#         tub=True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for x in range(2,n):
#                 if n%x==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(n)
         
#     return tub_sonlar

# print(oraliq(1,30))

def ketma_ketlik(son):
    finobachchi=[]
    for n in range(son):
        if n==0 or n==1: 
            finobachchi.append(n)
        else:
            finobachchi.append(finobachchi[n-1]+finobachchi[n-2])
    return finobachchi

print(ketma_ketlik(10))


    

    
    