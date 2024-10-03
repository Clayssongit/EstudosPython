class Animal:
    name = ""
    size = ""
    color = ""

    def eat(self):
        print("Animal se alimentando")

class Horse(Animal):
    race = ""

    def escape(self):
        print("cavalo fugindo")

class Leon(Animal):
    mane = True

    def hunt(self):
        print("Leão caçando")

h=Horse()
h.name="Carpeado"
h.color="Preto"
print(h.name)
h.escape()
h.eat()

print("")

l=Leon()
l.name="Simba"
l.color="Marrom"
print(l.name)
l.hunt()
l.eat()