#!/usr/bin/env python3
import re


def retira_formatacao(num_cpf):
    formatado = re.sub('\D', '', num_cpf)
    return valida_cpf(formatado)


def valida_cpf(num_cpf):
    if len(num_cpf) != 11:
        return("Precisa ter 11 numeros")
    else:
        ele = num_cpf[0]
        chk = True
        for item in num_cpf:
            if ele != item:
                chk = False
                break
    
        if (chk == True):
            return "todos os digitos repetidos não devem ser aceitos"
        else:
            return (num_cpf)

cpf = input("Digite o CPF:")
print(retira_formatacao(cpf))
