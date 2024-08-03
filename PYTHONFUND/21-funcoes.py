# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello World")  
wellcome()

# 2 - Função que soma dois números
def sum():
    return 5 + 4
print(sum())

# 3 - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
    gamePrice = float(input("Digite o preço do jogo: "))
    noteRating = float(input("Digite a nota de avaliação do jogo: "))
    print(f"{name} - R$ {gamePrice}")
create_game()