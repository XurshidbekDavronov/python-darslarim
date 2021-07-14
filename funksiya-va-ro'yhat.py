# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:49:04 2021

@author: admin
"""

# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['ali','vali','soli','hasan','husan']
# # baholar=bahola(talabalar)#bunda talabalar ro'yhati bo'shab qoladi
# baholar=bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# def katta_harf(ismlar):
#     ruyhat=[]
#     while ismlar:
#         ism=ismlar.pop()
#         ruyhat.append(ism.title())
#     return ruyhat
# nomlar=['ali','vali','soli','hasan','husan']
# nomlar.reverse()
# ruyhat=katta_harf(nomlar)
# print(ruyhat)
# print(nomlar)

# def katta_harf(ismlar):
#     ismlar=ismlar[:]
#     for i in range(len(ismlar)):
#         ismlar[i]=ismlar[i].title()
#     return ismlar
# nomlar=['ali','vali','soli','hasan','husan']
# ruyhat=katta_harf(nomlar)
# print(ruyhat)
# print(nomlar)

def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar
talabalar=['ali','vali','soli','hasan','husan']
# baholar=bahola(talabalar)#bunda talabalar ro'yhati bo'shab qoladi
baholar=bahola(talabalar[:])
print(baholar)
print(talabalar)