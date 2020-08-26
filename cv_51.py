"""
Vytvořme program, který nám seřadí abecedně jakýkoli list. Nemůžeme použít funkce jako je sort() nebo sorted(). Toto cvičení slouží jako procvičení práce s for + break + else.

Vytvoř list, do kterého vložíš jeden prvek z list names. Zároveň ho z listu names odstraň. Tento krok se ti bude hodit, když budeš chtít přidávat a seřazovat další jméno z listu names do listu sorted_names

Vytvoř vnořený for loop

vnější for loop, kterým budeš procházet seznam names (měl by mít už o jeden prvek méně)

vnitřní for loop, kterým budeš procházet seznam sorted_names a pomocí podmínkového výrazu, break a else vlož jméno z names buď na pozici, nebo za pozici

Vytiskni seřazená jména
"""

sorted_names = []

names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

sorted_names.append(names.pop())

for name in names:
    for index, sort_name in enumerate(sorted_names):
        if name < sort_name:
            sorted_names.insert(index, name)
            break
    else:
        sorted_names.append(name)

print(sorted_names)


