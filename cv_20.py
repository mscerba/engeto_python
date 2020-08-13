# vytvorte slovnik s nazvem 'film'
film = {"name": "Shawshank Redemption", "rating": 87, "year":1994, "director": "Frank Darabont"}

# do slovniku pridejte 2 nove kategorie
film["starring"] = ["Tim Robbins", "Morgan Freeman"]
film["budget"] = 200

# vymazte chybne vytvorenou kategorii 'budget'
del film["budget"]

# vytvorte novy slovnik
films = dict()

# do nove vytvoreneho slovniku vlozte pod klic 'drama' film
films["Drama"] = film
print(films)

# vypise zanry, ktere nase databaze nabizi
print('We can currenty offer... ')
print(list(films.keys()))

# vyber zanru
genre_film = input('What genre are you interested in: ')
print('HERE IT GOES: ')
print(films[genre_film])

# vymazani databaze a informacni hlasky
erase_db = input('You want to delete the database (a/n): ')

if erase_db == "a":
    film.clear()
    print('DATABASE HAS BEEN ERASED')
    print(films['Drama'])
else:
    print('Thank you for not deleting me')

