"""
Conta letras maiúsculas e minúsculas:
-> Escreva uma função em Python que receba uma string e conte o número de letras
 maiúsculas e minúsculas desta string.
"""
# def conta_String():
#     cont_Ma = 0
#     cont_Mi = 0
#     string = input("Digite seu texto: ")

#     for i in string:
#         if i.isupper():
#             cont_Ma += 1
#         elif i.islower():
#             cont_Mi += 1
#         else:
#             print("Caracter incorreto")
#     print(f"Seu texto possui {cont_Ma} letras maiúsculas e {cont_Mi} letras minúsculas.")
# conta_String()


"""
Lista números pares e ímpares de uma lista:
-> Escreva uma função Python para imprimir os números pares e ímpares
em duas listas separadas para cada uma.
"""
def par_impar(valor):
    par = []
    impar = []
    for i in range(valor):
        num = int(input("Digite os valores que deseja guardar: "))
        if num %2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print(f"Lista de par {par} e lista de impar {impar}.")
qts = int(input("Digite quantas vezes: "))
par_impar(qts)
