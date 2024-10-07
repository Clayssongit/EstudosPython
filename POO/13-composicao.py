class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
class Fish(Animal):
        race = ""
    
class Parrots(Animal):
        color = ""
        
class Zoo:
    def __init__(self):
        self.animals_dict = {}
    
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f" No nosso zoológico temos {result} quantidade de {category}"
    
zoo = Zoo()
peixe = Fish("Nemo", "Mamíferos")
papagario = Parrots("Louro", "Aves")
peixe2 = Fish("Botato", "Mamíferos")
print(vars(peixe))
print(vars(papagario)) 
zoo.add_animal(peixe)
zoo.add_animal(papagario)
zoo.add_animal(peixe2)
print(zoo.total_of_category("Aves"))
print(zoo.total_of_category("Mamíferos"))