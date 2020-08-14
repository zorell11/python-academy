# Vytvořte nový skript films.py. Uvnitř skryptu vytvořte slovník film, který bude uchovávat následující informace:
#name = 'Shawshank Redemption'
#rating = 87
#year = 1994
#director = 'Frank Darabont'
# -Do skriptu films.py napiš kód, který do slovníku 'film' přidá 2 nové kategorie
# -První kategorie by měla mít název 'starring' a měla by být asociována s listem obsahujícím tyto stringy: 'Tim Robbins', 'Morgan Freeman'.
# -Druhá kategorie s názvem 'budget' by měla nést hodnotu 200
# -Teď vám došlo, že kategorii 'budget' v databázi nechcete a rozhodli jste se ji smazat. Smažte tedy celý pár klíč-hodnota pod klíčem 'budget'.
# -Nyní vytvořte nový slovník s názvem films.
# -Přidejte slovník pod proměnnoufilm do nově vytvořeného slovníku films pod klíč 'DRAMA'.
# Do konzole vypište obsah proměnné films: Příklad běžícího programu:
#~/PythonBeginner/Lesson2 $ python films.py
#{'DRAMA': {'year': 1994, 'starring': ['Tim Robbins', 'Morgan Freeman'], 'rating': 87,
#'director': 'Frank Darabont', 'name': 'Shawshank Redemption'}}
#Všimněte si, že pořadí, ve kterém jsou kategorie vytištěny, se nemusí shodovat s pořadím, ve kterém byly napsány.
#Tak! A máme malou (velmi malou) filmovou databázi. Nyní uživatelům umožníme získávat informace o filmech z databáze.
#Uživatel by měl mít možnost získat informace o filmech podle jejich žánru. Zkuste napsat kód, který bude po spuštění fungovat přibližně takto:
#~/PythonBeginner/Lesson2 $ python films.py
#We can currently offer:
#['DRAMA']
#What genre are you interested in? DRAMA
#HERE IT GOES:
#{'year': 1994, 'starring': ['Tim Robbins', 'Morgan Freeman'], 'rating': 87, 'director':
#'Frank Darabont', 'name': 'Shawshank Redemption'}
#Posledním úkolem je napsat příkaz, který vymaže celý slovník 'films' a poté do konzole vypíše zprávu DATABASE HAS BEEN ERASED:.
#Příklad běžícího programu:
#~/PythonBeginner/Lesson2 $ python films.py
#We can currently offer:
#['DRAMA']
#What genre are you interested in? DRAMA
#HERE IT GOES:
#{'year': 1994, 'starring': ['Tim Robbins', 'Morgan Freeman'], 'rating': 87, 'director': 'Frank Darabont', 'name': 'Shawshank Redemption'}
#DATABASE HAS BEEN ERASED:
#{}
###################
film = dict( name = 'Shawshank Redemption', rating = 87, year = 1994, director = 'Frank Darabont')
film.update(starring = ['Tim Robbins', 'Morgan Freeman'], budget = 200)
del film['budget']
films = dict()
films['DRAMA'] = film
print(films)

print('We can currently offer:\n', list(films))

genre = input('What genre are you interested in? ')
print('HERE IT GOES:\n', films[genre])

films.clear()
print('DATABASE HAS BEEN ERASED:\n',films)
