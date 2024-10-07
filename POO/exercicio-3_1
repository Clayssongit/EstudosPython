from exercicio3 import Trip

trip0 = Trip("Lençóis Maranhence")
trip1 = Trip("São Paulo")
trip2 = Trip("Gramado")
trip3 = Trip("Rio de Janeiro")
trip4 = Trip("Caldas Novas")

print("Olá viajante. Temos algumas opções de viagem para você.")

traveler = input("Digite seu nome para começar: \n")
print (f"{traveler}, Temos 5 destinos que combinam com você"
       """
       [0] - Lençóis Maranhence
       [1] - São Paulo
       [2] - Gramado
       [3] - Rio de Janeiro
       [4] - Caldas Novas
       """
       
       )
choice = int(input("Selecione o destino da sua viagem: "))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >=5:
        print("Opção invalida")
        break
    else:
        print(f"{traveler}, Sua viagem para {list_trip[choice].destiny} está marcada") #Busca na lista o choice no atributo destiny"
        print("Boa viagem!")
        break