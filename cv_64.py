"""
Ověření pomocí Luhnova testu vypadá následovně:

Obrátí se pořadí číslic v čísle.
Vezme se první, třetí...a každá další lichá číslice v tomto obráceném pořadí a sečte do sumy s1.
Potom se vezme druhé, čtvrté...a každá sudá číslice a: a. Každá číslice se vynásobí dvěma. Pokud je číslo získané násobením větší než 9, sečteme jeho číslice. b. Sečteme všechny sudé číslici, které prošli násobením a upravením do s2.
Pokud s1 + s2 končí 0, potom lze původní číslo považovat za platné číslo kreditní karty.
Výstupem programu by měly být hodnoty True nebo False v závislosti na tom, jestli je dané číslo platební karty platné, nebo ne.

Když je číslo platební karty 49927398716, vypadá to takhle:

# Obracene poradi:
  61789372994
# Suma lichych cislic:
  6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
# Sude cislice:
    1,  8,  3,  2,  9
# Kazda suda vynasobena dvema:
    2, 16,  6,  4, 18
# Secteni cislic kazdeho nasobeni
    2,  7,  6,  4,  9
# Suma upravenych sudych cislic
    2 + 7 + 6 + 4 + 9 = 28 = s2
# Suma s1+s2 koncici 0:
  s1 + s2 -> 70
# Funkce vrati
True

Příklad fungující funkce:

luhn(61789372994)
True
"""


credit_card = 49927398716

def luhn(number):
    number = str(number)
    s1 = 0
    s2 = 0
    for index, num in enumerate(number[::-1]):
        if index % 2 == 0:
            s1 += int(num)
        elif index % 2 != 0:
            num_devide = int(num) * 2
            if num_devide <= 9:
                s2 += num_devide
            else:
                n1 = str(num_devide)[0]
                n2 = str(num_devide)[1]
                s2 += int(n1)+int(n2)
    return True if (s1 + s2) % 10 == 0 else False






print(luhn(credit_card))

