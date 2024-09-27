"""
1 - O método de classe utiliza o parâmetro referente a classe.
2 - O método de classe pode acessar ou modificar o estado da classe.
3 - Usamos o decorator @classmethod para um método de classe.
"""

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return (f"Console {self.name}, está por R${self.price}.")
    
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    
nitendo = Console.from_text("Meu vídeo game é Nitendo e o preço é 1980 reais")
ps5 = Console.from_text("Meu outro vídeo game é ps5 e o valor dele é 3500 reais")
ps3 = Console("ps3", 2000)
print(nitendo.__dict__)
print(ps3)