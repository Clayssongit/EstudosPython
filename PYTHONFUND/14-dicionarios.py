gameFifa = {
    "name": "fifa 23",
    "yearLaunch": 2022,
    "gamePrince": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionario
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Recuperar apenas as chaves do dicinario
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionario
print(gameFifa.values())

# 4 - Buscar itens do dicionario com chave e valor (Retornando em tuplas)
print(gameFifa.items())

# 5 - Adicionar itens ao dicionario
gameFifa["players"] = 2
gameFifa["times"] = 57
print(gameFifa)

# 6 - Atualizar itens do dicionario
gameFifa.update({"players": 1})
gameFifa.update({"times": 50})
print (gameFifa)

# 7 - Remover itens do dicionario
gameFifa.pop("players")
print(gameFifa)