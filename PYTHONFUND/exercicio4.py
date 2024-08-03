# 1 - Contagem regressiva de lançamento.
import time, winsound

frequency = 7000
duration = 2000
contagem = 10

while contagem > -1:
    print (contagem)
    contagem -= 1
    time.sleep(1)
winsound.Beep(frequency, duration)
print('=====FOGUETE LANÇADO=====')