import random

# 1 - Seleciona valor aleatório de uyma lista
list1 = [7, 4, 3, 2, 5, 8, 3, 1, 3]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 20)
print(r1)

# 3 - Selecionar caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 3))
print(random.sample(list1, 2))
print(random.sample(name, 3))