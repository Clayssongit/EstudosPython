"""
* Advinhe o Número
-> Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número.

"""
import random

done = False

while not done:
    print("Oque você deseja fazer?")
    print("1. Advinha o número")
    print("2. Sair")

    choice = input(">")

    if choice == "1":
        print("====Advinhe um número de 1 a 10====\n")
        number = int(input("Digite um número de 1 a 10\n"))
        result = random.randint(1,10)
        if number == result:
            print("Parabéns! Você acertou! ")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 2")