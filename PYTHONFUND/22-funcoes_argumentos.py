# 1 - crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(Fname, Lname):
    print(f"Nome completo: {Fname} {Lname}")
full_name("Claysson", "Eugenio")

# 2 - Crie uma função que some dois números via parâmetros
def sum(a, b):
    return a + b
print(sum(4, 4))

# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtsRating):
    game_name = input("Digite o nome do jogo: ")
    sum = 0
    for i in range(qtsRating):
        note = float(input("Digite a nota para o jogo: "))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum / qtsRating}")
rating = int(input("Digite quantas avaliações deseja fazer do jogo: "))
rating_game(rating)
rating_game(rating)
