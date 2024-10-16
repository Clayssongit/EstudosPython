"""
*Gerenciamento de Jogadores e Times:
-> Escreva um programa em python que realize o gerenciamento de Jogadores.
Ele deve atender aos seguintes requisitos:

1 - A opção de listas os times deve mostrar o índice, o nome e a quantidade
de jogadores do time.
2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir o índice especifico do time que foi cadastrado
para fazer a sua exclusão.
4 - A opção de adicionar um jogador em um time deve pedir um índice do time que foi
cadastrado e associar com o nome do jogador que será adicionado.
5 - A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e 
utilizar esse índice para remover o jogador que for cadastrado no time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar
os jogadores que foram associados a ele.
"""

teams = {}
done = False

#Função para Listar times
def print_teams():
    print("Times Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']}({len(team['players'])} jogadores)")

#Função para Listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

while not done:
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")


    choice = input(">")
    if choice == "1":
        team_name = input("Digite o nome do time: ")
        teams[team_name] = {'name': team_name, 'players':[]}
        print("Time adicionado.")
    elif choice == "2":
        print_teams()
        team_num = int(input("Número do Time para ser removido: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time removido")
        else:
            print("Número do Time invalido")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe um núemro do time que deseja adicionar um jogador:"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time!")
        else:
            print("Número invalido")
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe um núemro do time que deseja remover o jogador:"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover: "))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num -1]
                print("Jogador removido")
            else:
                print("Núemro do jogador invalido")
        else:
            print("Núemro do time invalido")


    elif choice == "6":
        print_teams()
        team_num = int(input("Informe um núemro do time que deseja listas os jogador:"))
        if team_num <= len(teams):
             team_name = list(teams.keys())[team_num -1]
             print_team_players(teams[team_name])
        else:
            print("Número invalido")
    elif choice == "7":
        done = True
    else:
        ("Opção invalidade")