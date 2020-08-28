"""
Vaším úkolem je vytvořit funkci gcd (), která vypočítá největšího společného dělitele dvou celých čísel.

Jak vypočítat GCD:
Můžeme použít operátor modulo k opakovanému výpočtu zbytku dělení mezi čísly A a B. Pokud se zbytek! = 0, pak se A stane
 B a B se stane zbývající v následující iteraci. To se provádí, dokud zbytek dělení mezi A a B nebude 0.

gcd(414,78)
6
gcd(414,49)
1

"""


def gcd(num_1, num_2):
    while num_1 % num_2 != 0:
        result = num_1 % num_2
        num_1 = num_2
        num_2 = result
    return num_2

print(gcd(414,49))


