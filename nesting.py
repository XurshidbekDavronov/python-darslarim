# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:46:49 2021

@author: admin
"""

#car0 = {
#        'model':'lasetti',
#        'rang':'oq',
#        'yil':2018,
#        'narx':13000,
#        'km':50000,
#       'korobka':'avtomat'
#        }

#car1 = {
#        'model':'nexia 3',
#        'rang':'qora',
#        'yil':2015,
#        'narx':9000,
#        'km':89000,
#        'korobka':'mexanika'
#        }

#car2 = {
#        'model':'gentra',
#        'rang':'qizil',
#        'yil':2019,
#        'narx':15000,
#        'km':20000,
#        'korobka':'mexanika'
#        }

#car=car0
#print(f"{car['model'].upper()} "
#      f"{car['rang']} rang, {car['yil']}-yil, {car['narx']} $")
#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].upper()} "
#      f"{car['rang']} rang, {car['yil']}-yil, {car['narx']} $")
#print(f"{cars[0]['model'].title()}")

#malibus=[]
#for i in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None,
#        'yil':2021,
#        'narx':None,
#        'km':0,
#        'korobka':'avto'
#        }
#    malibus.append(new_car)
#for malibu in malibus:
#    print(malibu)
#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
   
#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
   
#for malibu in malibus[6:]:
#    malibu['rang']='qora'
#    malibu['korobka']='mexanika'
#for malibu in malibus:
#    if malibu['korobka']=='avto': 
#        malibu['narx']=40000
#    else:
#        malibu['narx']=35000
#    print(malibu)
#dasturchilar = {
#    'ali':['pyton', 'C++'],
#    'vali':['c#', 'php'],
#    'soli':['css','js'],
#    'komil':['c++','sql'],
#    }  
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi tillarni biladi:")
#    for til in tillar:
#        #print(f"{til.upper()}")
#        print(f"{til.upper()}")
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi tillarni biladi:", end=' ')
#    for til in tillar:
#        #print(f"{til.upper()}")
#        print(f"{til.upper()}", end=' ')
#adib0={
#       'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#       't_yil':810,
#       'shahri':'Buxoro',
#       'yosh':'60'
#       }               
#adib1={
#       'ism':'Abdulla Qodiriy',
#       't_yil':1894,
#       'shahri':'Toshkent',
#       'yosh':'44'
#       }
#adib2={
#       'ism':'Erkin vohidov',
#       't_yil':1936,
#       'shahri':'Farg\'ona',
#       'yosh':'80'
#       }
#adib3={
#       'ism':'Alisher Navoiy',
#       't_yil':1441,
#       'shahri':'Xirot',
#       'yosh':'60'
#       }
#adiblar=[adib0, adib1, adib2, adib3]
#for adib in adiblar:
#    print(f"{adib['ism'].title()} {adib['t_yil']}-yilda {adib['shahri']}"
#          f"da tavallud topgan, {adib['yosh']} umr ko'rgan")
#adib0['asar']='Al-jome as-sahih','Al-adab al_mufrad','At-tarix al-kabir','At-tarix as-sag\'ir'
#adib1['asar']='O\'tgan kunlar', 'Mehrobdan chayon','Obid ketmon'
#adib2['asar']='Tong nafasi','Qo\'ishiqlarim sizga','O\'zbegim','Qiziquvchan matmusa'
#adib3['asar']='Xamsa', 'Lison ut-tayr','Mahbub ul-qulub','Munojot'
#for adib in adiblar:
#    print(f"\n{adib['ism'].title()}ning mashxur asarlari:")
#    asar=adib['asar']
#    for kitob in asar:
#        print(kitob)
#kinolar = {
#    'ali':['Terminator', 'Rembo', 'Titanik'],
#    'vali':['Tenet', 'Inception', 'Interstellar'],
#    'soli':['Abdullajon','Bomba', 'Shaytanat'],
#    'komil':['Mahallada duv-duv gap','John Wick','Sangam'],
#    }  
#for ism, kino in kinolar.items():
#    print(f"\n{ism.title()}ning sevimli kinolari:")
#    for film in kino:
#        print(film)
davlatlar ={
    "O'zbekiston" :{
                'poytaxt':'Toshkent',
                'hudud':448978,
                'aholisi':33000000,
                'pul':'so\'m'
                },
    "Rossiya ":{'poytaxt':'Moskva',
                 'hudud':17098246,
                 'aholisi':144000000,
                 'pul':'rubl'
                },
      "AQSH ":{
                  'poytaxt':'Vashington',
                  'hudud':9631418,
                  'aholisi':327000000,
                  'pul':'dollar'
                  },
       "Malayziya ":{
                   'poytaxt':'Kuala-Lumpur',
                   'hudud':329750,
                   'aholisi':25000000,
                   'pul':'rinngit'
                   }
           }   
#for davlat, info in davlatlar.items():
davlat=input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar.items():
    info=davlatlar[davlat]
    print(f"\n{davlat}ning poytaxti {info['poytaxt.title()']}"
          f"\nHududi: {info['hudud']} kv.km"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul']}")
else:
    print('Bunday davlat ma\'luloti yo\'q')
    