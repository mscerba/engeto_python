"""
Tvým úkolem bude vytvořit funkci, která imituje built-in funkci sum(). Vstup bude sekvence čísel a výstup suma těchto čísel.

Příklad použítí naší funkce my_sum() v Pythonu:

sequence = [32,43,54,54,76,21,62,83,52,58]
my_sum(sequence)
535
"""

def my_sum(seq):
    result = 0
    for i in seq:
        result += i
    return result

sequence = [32,43,54,54,76,21,62,83,52,58]
print(my_sum(sequence))

