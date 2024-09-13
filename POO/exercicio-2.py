"""
* Classe Produto e método desconto
Desenvolva uma classe em Python para atender as
seguintes especificidades de um Produto:

1 - Cada produto deve ter um preço e um nome.
2 - A Classe deve ter um método construtor e o método dundle str.
3 - A Classe deve ter um método para desconto.
O método deve receber o desconto em percentual e realizar 
O cálculo de quanto ficaria o preço final com o desconto.
"""

class Produto:

    def __init__(self, name, valor ):
        self.name = name
        self.valor = valor
    
    def __str__(self):
        return f"Produto: {self.name} - R$ {self.valor} reais"
    
    def desconto(self, perc_discout):
        v_desonto = (self.valor/100) * perc_discout
        final_price = self.valor - v_desonto
        return float(final_price)

detergente = Produto("Detergente", 2.5)

print (detergente.desconto(10))
