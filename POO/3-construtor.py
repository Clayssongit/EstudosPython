class Movie:
    def __init__(self, name, yearLauch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLauch = yearLauch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
#Para evitar erro ao buscar um objeto podemos adicionar o def __str__
    def __str__(self):
        return f"Filme: {self.name}"
#Importante sempre adicionar os itens em ordem do construtor. 
movie = Movie("Super Mario Bros", 2023, False, 5.0, 130)
print(movie.name)