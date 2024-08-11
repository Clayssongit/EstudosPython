import os 
import time

def off30m():
    shutdown = input("Você quer desligar seu computador: sim/não? ")
    
    if shutdown == 'não':
        exit()
    else:
        time.sleep(10)
        os.system("shutdown /s /t 1")
    
def off1h():
    shutdown = input("Você quer desligar seu computador: sim/não? ")
    
    if shutdown == 'não':
        exit()
    else:
        time.sleep(3600)
        os.system("shutdown /s /t 1")
        
off30m()