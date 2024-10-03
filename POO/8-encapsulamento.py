"""
Para deixar um attributo de class privada adicione '__'.
"""

class Enployee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show(self):
        print(f"Nome {self.name} - Salário {self.salary}")

mario = Enployee("Mario", 4000)
maria = Enployee("Maria", 5000)