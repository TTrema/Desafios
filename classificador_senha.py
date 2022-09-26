#!/usr/bin/env python3

import re
#from ssl import _PasswordType

senha = input(r"Digite a senha a ser avaliada:")

def classifica_senha(pwd):
    if len(pwd) == 0:
        return "Digite uma senha"
    if len(pwd) <= 7:
        return 0
    else:    
        password_scores = {0:0, 1:0, 2:1, 3:2}
        password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num', 'has_spec'], False)
        if re.search(r'[A-Z]', pwd):
            password_strength['has_upper'] = True
        if re.search(r'[a-z]', pwd):
            password_strength['has_lower'] = True
        if re.search(r'[0-9]', pwd):
           password_strength['has_num'] = True
        if re.search(r'[^a-zA-Z0-9]', pwd):
           password_strength['has_spec'] = True


        score = len([b for b in password_strength.values() if b])
        return password_scores[score]
    

print (classifica_senha(senha))


#_PasswordType.split() 