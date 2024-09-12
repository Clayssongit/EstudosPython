class Movie:
    def __init__(self, name, yearLauch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLauch = yearLauch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"

#Função para Imprimir todos os dados da ficha
    def techinal_sheet(self):
        print("### Dados do Filme ###")
        print(f"Nome do filme: {self.name} ")
        print(f"Ano de lançamento: {self.yearLauch} ")
        print(f"Incluso no plano? {self.includedPlan}")
        print(f"Nota do Filme: {self.note}")
        print(f"Duração do filme: {self.durationMinutes}")

mario = Movie("Super Mario Bros", 2023, False, 5.0, 120)
top_gun = Movie("Top Gun Maverick", 2022, True, 4.5, 160)
mario.techinal_sheet()
print('\n')
top_gun.techinal_sheet()