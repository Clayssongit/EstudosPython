"""
* Cadastro de Viagem
    Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:
    
    1 - Usuário deve informa o seu nome para cadastrar uma viagem.
    2 - Usuário deve selecionar um destino com base nas instâncias de objetos de classe viagem.
    3- Deve ser apresentado uma mensagem indicando que o cadastro
        da viagem no destino específico foi feito com sucesso.
"""
class Trip:
    def __init__(self, destiny):
        self.destiny = destiny
