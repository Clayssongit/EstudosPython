import os 

def off_30m():
    shutdown = input("Você quer desligar seu computador: sim/não? ")
    
    if shutdown == 'não':
        exit()
    else:
        os.system("shutdown /s /t 1800")
    
def off_1h():
    shutdown = input("Você quer desligar seu computador: sim/não? ")
    
    if shutdown == 'não':
        exit()
    else:
        os.system("shutdown /s /t 3600")
        
# para cancelar desligamengo utilize:
# os.system('shutdown /a')

def cancel_shutdown():
    os.system('shutdown /a')