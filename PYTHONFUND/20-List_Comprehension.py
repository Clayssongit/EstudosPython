# 1 - Liste valores de 0 a 10 que sejam menor do que 4.
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Mario odyssey", "Dk Coutry",
             "Luigis Mansion", "Kirby"]

# 2 - Jogos que possuem a Letra a.
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [y for y in gamesList if y != "Kirby"]
print(gamesFinished)