class Movie:
    def __init__(self, name, yearLauch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLauch = yearLauch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

movie = Movie("Super Mario Bros", 2023, False, 5.0, 130)
print(movie.name)