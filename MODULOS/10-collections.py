from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pêra",
          "Tangerina", "Uva", "Laranja",
          "Abacaxi", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa23", 90.50, 8.5)
g2 = game("Resident Evil 4", 300, 10.0)
print(g1)
print(g2) 