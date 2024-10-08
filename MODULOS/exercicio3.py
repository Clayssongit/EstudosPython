import re

"""
* Verificar conteúdo da string 
-> Escreva um programa em Python para verificar se uma string 
contém apenas um determinado conjunto de caracteres (neste caso, a-z, 
A-Z e 0-9).
"""

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]') # compile possibilita passar mais de uma regra
    string = rule.search(string)
    return not bool (string) 

print(check_character('102930123910mksdmfsakfdnaAKNSA'))
print(check_character('102930123910mksdmf#@$*&!'))