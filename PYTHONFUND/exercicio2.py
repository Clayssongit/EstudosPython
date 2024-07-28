#Substituindo caractere repetido:
nome = "fifa 23"

print(nome.capitalize().replace("f", "$"))


#Troca de caracteres:
"""Escreva um programa em python para obter uma única string de duas strings fornecidas,
separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc xyz -> xyc abz
"""
name1 = "abc"
name2 = "xyz"
new_name1 = name2[:2] + name1[2:]
new_name2 = name1[:2] + name2[2:]
print(new_name1 + ' ' + new_name2)