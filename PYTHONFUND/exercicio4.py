# 1 - Contagem regressiva de lançamento.
# import time, winsound

# frequency = 6000
# duration = 2000
# contagem = 10

# while contagem > -1:
#     print (contagem)
#     contagem -= 1
#     time.sleep(1)
# winsound.Beep(frequency, duration)
# print('=====FOGUETE LANÇADO=====')

# 2 - faça um progrma que calcule a tabuada de um número, com valores iniciais  e finais 
# informados pelo usuario
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número inicial: '))
num3 = int(input('Digite até qual número deve fazer a conta: '))
oper = input("Digite o operador (+, -, *, /): ")

for i in range(num2, num3 + 1):
    if oper == '+':
        resultado = num1 + i
    elif oper == '-':
        resultado = num1 - i
    elif oper == '*':
        resultado = num1 * i
    elif oper == '/':
        resultado = num1 / i
    else:
        print("Operador inválido")
        break
    print(f"{num1} {oper} {i} = {resultado:.2f}")