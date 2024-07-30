import pprint
gamesDict = {
    "residente evil 4":{
        "yearLauch": 2023,
        "classification": 9.8,
        "genre":["ação", "aventura"]
    },
    "mario odyssey":{
        "yearLauch": 2017,
        "classification": 10.0,
        "genre":["ação", "3d"]
    },
    "donkey kong country":{
        "yearLauch": 1995,
        "classification": 9.5,
        "genre":["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionário aninhado
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adidiconar novos itens
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dicionário
del gamesDict["residente evil 4"]
pp.pprint(gamesDict)

# 4 - Busca apenas os nomes dos dicionários filhos
jogos = gamesDict.keys()
print(list(jogos))