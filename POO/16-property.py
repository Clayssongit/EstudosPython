class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property # metodo para o getter
    def name(self):
        return self.name
    
    @name.setter # metodo para setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma String")
        self._name = value #Deixar protegido com _

pessoa = Person("Pedrocas", 12)
print(vars(pessoa))