# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 09:04:47 2021

@author: admin
"""

#talaba = {'ism':'Xurshid', 'familiya':'Davronov', 'yosh':35, 'fakultet':'informatika', 'kurs':4}
#for kalit, qiymat in talaba.items():
#    print(f"Kalit: {kalit.upper()}")
#    print(f"Qiymat: {qiymat}\n")

#telefon ={
 #   'ali':'iphone 9',
  #  'vali':'samsung 8',
   # 'soli':'nokia x',
    #'anvar':'mi 8 pro'
    #} 
#for k,q in telefon.items(): #items() qiymat elementlarini chiqaradi
 #   print(f"{k.title()}ning telefoni {q.upper()}")
#mahsulotlar ={
 #   'olma': 5000,
  #  'anor': 20000,
   # 'anjir': 3000,
    #'shaftoli': 70000
    #}  
#print(mahsulotlar.keys())

#mahsulotlar['uzum']=11000
#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
 #   print(f"{mahsulot.upper()}")

#bozorlik=['olma', 'uzum', 'non', 'kartoshka']
#for mahsulot in mahsulotlar: #keys() metodini qo`yib ketsa ham bo`ladi
 #   if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#for narsa in bozorlik:
 #   if narsa not in mahsulotlar:
  #      print(f"Iltimos do'koningizga {narsa} ham olib keling")
#print("Do'kondagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar.keys()):#sorted() tartiblab chiqadi
 #   print(f"{mahsulot.upper()}")
#print('Foydalanuvchilar ishlatadigan telefonlar')
#for tel in telefon.values():
 #   print(tel.upper())
#telefon['samad']='iphone 9'
#telefon['nodir']='samsung 8'
#telefon['karim']='iphone 9'
#print(telefon)
#print('Foydalanuvchilar ishlatadigan telefonlar')
#for tel in telefon.values():
 #   print(tel.upper())
#print('Foydalanuvchilar ishlatadigan telefonlar')
#for tel in set(telefon.values()): #set() bir xil qiymatlarni bittasini oladi
 #   print(tel.upper())
#izohli_lugat = {
 #   'integer':'butun son',
  #  'float':"o'nlik son",
   # 'string':'satr, qator',
    #'list':"ro'yhat",
    #'tuple':"o'zgarmas ro'yhat",
    #'del':"o'chirish",
    #'title':'bosh harf bilan chiqarish',
    #'upper':'barchasini bosh harfda chiqarish',
    #'lower':'barchasini kichik harfda chiqarish',
    #'boolen':'mantiqiy qiymat',
    #'for':'biror amalni takrorlaydi',
    #'if':'shart tekshirish operatori'
    #}
#for k,q in sorted(izohli_lugat.items()):
 #   print(f"{k.upper()} - {q}\n")
dunyo_davlatlari ={
    'AQSH':'Vashington',
    'Italiya':'Rim',
    "O'zbekiston":'Toshkent',
    "Qizg'iziston":'Bishkek',
    'Kanada':'Ottava',
    'Germaniya':'Berlin',
    'Malayziya':'Kuala Lumpur',
    'Xitoy':'Pekin',
    'Yaponiya':'tokio',
    'Fransiya':'Parij'
    }
#print('Dunyo davlatlari:')
#for davlat in sorted(dunyo_davlatlari):
#    print(davlat.upper())
    
#print('\nDavlatlar poytaxtlari:')
#for poytaxt in sorted(dunyo_davlatlari.values()):
#    print(poytaxt.title())
davlat=input("Qaysi davlatning poytaxtini bilishni istaysiz?: ").title()
poytaxt=dunyo_davlatlari.get(davlat)
if poytaxt==None:
        print(f"Kechirasiz,{davlat.title()} poytaxti haqida bizda ma'lumot yo'q")
else:
        print(f"{davlat.title()}ning poytaxti {poytaxt} shahri")
        