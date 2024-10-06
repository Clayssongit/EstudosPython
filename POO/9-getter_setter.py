class Enployee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")


#Metodo para buscar dados (get)
    def get_salary(self):
        return self.__salary
#Metodo para modificar atributos privados (set)
    def set_salary(self, salary):
        self.__salary = salary

mario = Enployee("Mario", 4000)
maria = Enployee("Maria", 5000)

mario.show()
mario.set_salary(7000)
mario.show()
