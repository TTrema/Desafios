#!/usr/bin/env python3
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def valida_numero(num):
   if num in range(0, 3999):
        return numero_para_romano(num)
      
      
   else: return "invalido"

def numero_para_romano(num):
    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman
    
numero = int(input("insira um numro de 0 a 3998:"))
print (valida_numero(numero))
#print (numero_para_romano(3998))

