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