"""
Vytvoř program, který vytiskne, kolikrát se každý objekt nachází v daném listu, tuplu, nebo stringu (u stringu chceme počet jednotlivých znaků).

Výstupem programu by měl být slovník, který se skládá z následující dvojice klíč - hodnota:

klíč - string reprezentace počítaného objektu,
hodnota - celé číslo, které značí počet výskytu daného objektu.

Celé číslo 1 se nachází v sekvenci 4x, číslo 8 se vyskytuje 1x, atd.

Zopakuješ si zde práci s:

podmínkovými výrazy,
sekvencemi,
slovníky,
for loop,
"""

seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

my_dict = {}

for i in seq:
    my_dict[i] = my_dict.get(i, 0) + 1

print(my_dict)

