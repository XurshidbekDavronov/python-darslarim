# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:52:24 2021

@author: admin
"""

# print('Kiritilgan sonni kvadratini chiqarish dasturi')
# savol='Istalgan son kiriting: '
# savol+="(Dastur tugashi uchun 'exit' deb yozing):"
# son=' '
# while son !='exit':
#     son=input(savol)
#     if son !='exit':
#         print(float(son)**2)
# print('Dastur tugadi')

# print('Kiritilgan sonni kvadratini chiqarish dasturi')
# savol='Istalgan son kiriting: '
# savol+="(Dastur tugashi uchun 'exit' deb yozing):"
# son=' '
# ishora=True
# while ishora:
#     son=input(savol)
#     if son =='exit':
#         ishora=False
#     else:
#         print(float(son)**2)
# print('Dastur tugadi')

# print('Kiritilgan sonni kvadratini chiqarish dasturi')
# savol='Istalgan son kiriting: '
# savol+="(Dastur tugashi uchun 'exit' deb yozing):"

# while True:
#     son=input(savol)
#     if son =='exit':
#         break
#     else:
#         print(float(son)**2)
# print('Dastur tugadi')

# sonlar =list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue 
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")
# print('Dastur tugadi')

#juft sonni topish
# son=0 
# while son<10:
#     son+=1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)
        
# #toq sonni topish
# son=0 
# while son<10:
#     son+=1
#     if son%2 ==0:
#         continue
#     else:
#         print(son)


# savol='Yoqtirgan kitobingiz nomini kiriting: '
# savol+="(Dastur tugashi uchun 'stop' deb yozing):"
# kitob=' '
# while kitob!='stop':
#     kitob=input(savol)
#     if kitob !='exit':
#         print(kitob)
# print('Dastur tugadi')

# savol='Yoshingizni kiriting: '
# savol+="(Dastur tugashi uchun 'exit' yoki 'quit' deb yozing):"

# while True:
#     yosh=input(savol)
#     if str(yosh)=='exit' or str(yosh)=='quit':
#         break
#     if int(yosh)<=6:
#             print('Chipta narxi 2000 so\'m')
#     elif int(yosh)>6 and int(yosh)<=18:
#             print('Chipta narxi 3000 so\'m')  
#     elif int(yosh)>18 and int(yosh)<=65:
#             print('Chipta narxi 10000 so\'m')
#     elif int(yosh)>65:
#             print('Chipta narxi bepul')
# print('Dastur tugadi')

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print('Dastur tugadi')