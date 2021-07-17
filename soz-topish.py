# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:49:52 2021

@author: admin
"""
import random
from uzwords import words

def soz_top():
    soz=random.choice(words)
    while '-'in soz or ' ' in soz:
        soz=random.choice(words)
    return soz.upper()

def displey(user_letters, word):
    displey_letter=""
    for letter in word:
        if letter in user_letters.upper():
            displey_letter+=letter
        else:
            displey_letter+='-'
    return displey_letter

def play():
    word=soz_top()
    #So'zdagi harflar
    word_letters=set(word)
    #Foydalanuvchi kiritgan harflar
    user_letters=''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    while len(word_letters)>0:
        print(displey(user_letters, word))
        if len(user_letters):
            print(f"Шу вақтга қадар киритган ҳарфларингиз:{user_letters}")
        
        letter=input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print(f"Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг:")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print(f"Бундай ҳарф йўқ. ")
        user_letters+=letter
    print(f"Табриклайман!!! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
            
    
        
