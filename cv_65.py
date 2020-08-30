"""
Cílem tohoto cvičení je vytvořit funkci, která příjímá list dvou nebo více stringů jako vstup a vrací boolean hodnotu, která nám říká, jestli všechny prvky uvnitř listu jsou anagramy, nebo ne.

#1 Pokud vložíme prázdný string, výstup by měl být False.
#2 Pokud vložíme list s jedním slovem, výstup by měl být True.



Příklad fungující funkce:

all_anagrams(['ship', 'hips'])
True
all_anagrams(['ship', 'hips', 'name'])
False
all_anagrams(['ship'])
True
all_anagrams([])
False
"""

def all_anagrams(words):
    if bool(words) == False:
        return False
    elif len(words) == 1:
        return True
    else:
        word_select = list(words.pop())
        word_len = len(word_select)
        for word in words:
            counter = 0
            for i in word_select:
                if i not in word:
                    return False
                else:
                    counter += 1
            if word_len == counter:
                break
        return True





words = ['ship', 'hips', 'psih']
print(all_anagrams(words))
