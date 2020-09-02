"""
V tomto cvičení budeme tvořit slovní hru šibenice. Ta je určena pro dva hráče, v tomto případě počítač
a člověk. Princip hry spočívá v tom, že se člověk snaží uhádnout slovo, které náhodně vybere počítač,
pomocí tipování jednotlivých písmen z hledaného slova.

Hádané slovo ve skriptu reprezentují podtržítka. Každé podtržítko reprezentuje jednotlivá písmena
daného slova. Pokud člověk tipne písmeno, které se nenachází v hledaném slově, počítadlo dostupných
pokusů se sníží o jednu hodnotu. Člověk vyhrává, pokud uhodne celé slovo v limitu povolených pokusů.
Naopak počítač vyhrává, když člověk vyčerpá všechny dostupné pokusy. Je na tobě, kolik pokusů bude mít
člověk k dispozici.

- musím ze seznamu slov vygenerovat náhodné slovo
- vygeruji podtrzitka -> vstup

2. musím vygenerovat náhodné slovo a podržítka: vstup -> písmeno, výstup -> odpověď, a místo podržítek
doplněna písmena

I am thinking of a word. What word is it?:
No, the letter 'C' is not in my word
Yes, there are 2 letters 'a'
"""


def kontrola():
    print('I am thinking of a word. What word is it?:')
    word = list(random_word())
    delka = len(word)
    counter = 0
    pokusy = delka
    znaky = list("_" * delka)
    print(" ".join(znaky))
    while counter != delka and pokusy != 0:
        vstup = input(f'Guess a letter ({pokusy} guesses available): ')
        if vstup not in word:
            print(f'No, the letter "{vstup}" is not in my word')
            pokusy -= 1
        else:
            for index, char in enumerate(word):
                char_count = 1
                if vstup == char:
                    znaky.pop(index)
                    znaky.insert(index, vstup)
                    counter += 1
                    char_count += 1
            print(f'Yes, there is {char_count} letter "{vstup}"')

        print(" ".join(znaky))


def random_word():
    import random
    words = ['jablko', 'kolo']
    return random.choice(words)



print(kontrola())

