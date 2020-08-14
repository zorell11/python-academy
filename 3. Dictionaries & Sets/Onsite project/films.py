film = {}

######################################################
film.update(name = 'Shawshank Redemption')
film.update(rating = 87)
film.update(year = 1994)
film.update(director = 'Frank Darabont')

film1 = dict()
film1['name'] = 'Shawshank Redemption'
film1['rating'] = 87
film1['year'] = 1994
film1['director'] = 'Frank Darabont'
print(film)
######################################################

film['starring'] = ['Tim Robbins', 'Morgan Freeman']
film['budget' ] = 200
print(film)
######################################################

film.pop('budget')
print(film)
######################################################

films = {}
films.update(DRAMA = film)
print(films)
######################################################

print("We can currently offer:")
print(list(films))

genre = input("What genre are you interested in? ")
print("HERE IT GOES:")
print(films[genre])
######################################################

print("DATABASE HAS BEEN ERASED:")
films.clear()
print(films)
