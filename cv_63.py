"""
Vytvoř funkci, která spočítá průměrnou hodnotu pro danou sekvenci číselných hodnot.

Příklad fungování funkce mean():

sequence = [32,43,54,54,76,21,62,83,52,58]
mean(sequence)
53.5
"""


def mean(seq):
    count = len(seq)
    result = 0
    for i in seq:
        result += i

    return result / count


sequence = [32,43,54,54,76,21,62,83,52,58]

print(mean(sequence))


