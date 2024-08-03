gameName = input("Digite o nome do jogo: ")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating != -1):
    rating = float(input("Informe a nota do jogo:"))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print("A média das avaliações do jogo {} foi de {:.2f}.".format(gameName, average))      