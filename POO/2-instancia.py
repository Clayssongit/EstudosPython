class Movie:
    name = ""
    yearLaunch = 0
    includedPLan = False
    note = 0 
    durationMinutes = 0

#Primeiro filme

movie = Movie()
movie.name = "Super Mario Bross"
movie.yearLaunch = '2023'
movie.includedPLan = False
movie.note = '5.0'
movie.durationMinutes = '130'
print("Dados do Filme##")
print(f"Nome do filme: {movie.name} \n Ano de lançamento: {movie.yearLaunch}")