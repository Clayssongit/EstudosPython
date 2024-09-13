'''
*Avaliação e Média de nota dos filmes
Desenvolva novas funcionalidades para complementar o nosso 
gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

1 - Uma das funcionalidades requeridas é que usuário possa realizar a 
avaliação de um filme passando uma nota com parâmetro e que essa nota
seja salva no atributo específico da classe.

2 - Assim que uma avaliação for realizada, deve ser incrementado o 
total de avalição daquele filme. Obs: Considere criar um atributo 
específico para esse fim.

3 - Para cada filme ter uma nota de avaliação média que consiste
na divisão do total de avaliação pelo total de avaliadores. 
'''

class Movie:
    def __init__(self, name, yearLauch, includedPlan, durationMinutes):
        self.name = name
        self.yearLauch = yearLauch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"

#Função para Imprimir todos os dados da ficha
    def techinal_sheet(self):
        print("### Dados do Filme ###")
        print(f"Nome do filme: {self.name} ")
        print(f"Ano de lançamento: {self.yearLauch} ")
        print(f"Incluso no plano? {self.includedPlan}")
        print(f"Nota do Filme: {self.totalEvaluation}")
        print(f"Duração do filme: {self.durationMinutes}")
        print(f"Total de Avaliadores: {self.evaluators}\n")
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def averege(self):
        print(f"Média do Filme {self.name}: {self.totalEvaluation / self.evaluators:.2f}\n")

mario = Movie("Mario Bros", 2023, False, 130)
avatar = Movie("Avatar", 2023, False, 160 )

mario.evaluate(9.5)
mario.evaluate(10)
mario.evaluate(8)
mario.techinal_sheet()
mario.averege()

avatar.evaluate(8)
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.techinal_sheet()
avatar.averege()