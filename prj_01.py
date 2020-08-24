TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


# 1 Na začátku přivítá uživatele.
print('-' * 60)
print('Welcome to the app. Please log in: ')

# 2 Vyžádá si od uživatele přihlašovací jméno a heslo.
# 3 Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

USERS = {'bob': 'heslo'}
setter = True

while setter:
    username = input('USERNAME: ')
    password = input('PASSWORD: ')

    if username not in USERS.keys() or password != USERS[username]:
        print('Špatné jméno nebo heslo! ')
    else:
        setter = False

print('-' * 60)


# 4 Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
print('We have 3 texts to be analyzed.')
text = int(input('Enter a number btw. 1 and 3 to select: '))

text_lst = TEXTS[text-1].split()
print('-' * 60)

# 5 Pro vybraný text spočítá následující statistiky:
count_words = len(text_lst)
index = 0
title_words = 0
lower_words = 0
upper_words = 0
numeric_str = 0
numeric_sum = 0

while index < count_words:
    word = text_lst[index]
    if word.istitle():
        title_words += 1
    elif word.islower():
        lower_words += 1
    elif word.isupper():
        upper_words += 1
    elif word.isnumeric():
        numeric_sum += int(word)
        numeric_str += 1
    index += 1

print(f'There are {count_words} words in the selected text.')
print(f'There are {title_words} titlecase words')
print(f'There are {upper_words} uppercase words')
print(f'There are {lower_words} lowercase words')
print(f'There are {numeric_str} numeric strings')
print('-' * 60)

# 6 Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
cetnost_slov = dict()

while text_lst:
    word = text_lst.pop().strip(',.')
    cetnost_slov[len(word)] = cetnost_slov.get(len(word), 0) + 1


while cetnost_slov:
    words = cetnost_slov.popitem()
    print(words[0], words[1] * '*', words[1])

print('-' * 60)

# 7 Program spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by tedy bylo číslo 8500:
print(f'If we summed all the numbers in this text we would get: {numeric_sum}')


