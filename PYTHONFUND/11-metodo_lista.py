gameList = ["Resident Evil 4", "Star Wars Jedi", 
            "The Legend of zelda", "Read Dead 2","Mario Odyssey",
            "Luigis Mansion 3"]

#1 - Tamanho da lista
print(len(gameList))

#2 - Recuperar um item da lista pelo índice
print(gameList.index("Mario Odyssey"))

#3 - Adicionar item ao final da lista
gameList.append("League of Legends")
print(gameList)

#4 - Ordenar a lista
gameList.sort()
print(gameList)

#5- Copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Star Wars Jedi")
print(gameReset)

#6 - Remove todos os itens da lista
gameList.clear()
print(gameList)