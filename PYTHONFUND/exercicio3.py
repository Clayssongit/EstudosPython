# Escreva um programa que pergunte a distância que um passageiro deseja percorrrer em km.
# Calcule o preço da passagem, corabranco r$ 0,50 por km para viagens de até 200km, e r$ 0,35 para viagens mais lonnga.

dKm = float(input("Digite a distância que deseja percorrer em KM: "))
if dKm <= 200:
    vFinal = (dKm*0.50)
else:
    vFinal = (dKm*0.35)
print ("O valor da sua passagem é: {:.2f}".format(vFinal))



# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento
# Para salários superiores a r$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%

sala = float(input("Digite seu salário: "))
perc_increase = 0.15
if sala > 1250:
    perc_increase = 0.10
perc_increase = sala * perc_increase + sala
print ("Seu salário atual com aumento é de {:,.2f}".format(perc_increase))


