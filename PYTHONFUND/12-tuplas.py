gamesTuple = ("Fifa 23", "Red Dead 2", "Star Wars",
              "Mario Odyssey", "The Legend of Zelda")
print(type(gamesTuple))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Busque o último iten da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo index
print(gamesTuple.index("Red Dead 2"))