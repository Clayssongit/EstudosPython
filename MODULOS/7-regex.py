import re

text = "OneBitCode: Transformamos pessoas em programadores sem limites"

# 1 - Índice inicial e final de palavras
# O r (em minúsculo), significa que estamos trabalhando com uma string bruta(row string)
match = re.search(r'pessoas em programadores' ,text)
print('Índice inicial', match.start())
print('Índice final', match.end())

# 2 - Buscando o Índice que possui o ponto
site = 'https://onebitcode.com'
match = re.search(r'\.', site) 
print(match)

# 3 - buscando um lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4 - Veriricando o inicio de uma string
rule = r'^A' # (^ siginifica o começo)
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for i in phrases:
    if re.match(rule, i):
        print(f"Corresponde: {i}")
    else:
        print(f"Não corresponde: {i}")

# 5 - Verificando o final de uma string
rule_end = r'!$' # ($ significa o final)
phrases2 = 'O dia está lindo!'
math = re.search(rule_end, phrases2)
if match:
    print('Sim, corresponde.')
else:
    print('Não conrresponde')