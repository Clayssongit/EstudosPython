gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online.
"""

print(len(gameDescription)) # Devolve quantidade de caracteres de uma lista
print(gameDescription.strip()) # Remove os espaços do inicio e final da lista. (MUITO IMPORTANTE PARA FORMULÁRIOS E TABELAS)
print(gameDescription.lstrip()) # Remove os espaços da esquerda da lista. 
print(gameDescription.rstrip()) # Remove os espaços da direita da lista.                                                                                     
print(gameName.upper()) # Retorna string em maiúsculo
print(gameName.lower()) # Retorna string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(20, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("f")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.count("a")) # Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro
print(gameDescription.split('3')) # Quebra string onde possuir a virgula ou função que for passada 
print(''.join(gameDescription)) # Junção de uma string. Caso queira apenas espaços deixa as aspas vazias